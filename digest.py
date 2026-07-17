"""
Agentic/Backend Content Digest
--------------------------------
Pulls recent posts from RSS feeds (Reddit natively, X/Twitter via an RSS
bridge you configure), filters them for relevance + recency, summarizes
them via OpenRouter's free models, and emails you the result.

Run this on a schedule (e.g. GitHub Actions, cron) every 2-3 days.

SETUP
1. Fill in FEEDS below with your RSS URLs (see config.py / README).
2. Set these environment variables (as GitHub Actions secrets, or locally):
   - OPENROUTER_API_KEY  -> your OpenRouter API key (free tier is fine)
   - SMTP_USER           -> the Gmail address you're sending FROM
   - SMTP_PASS           -> a Gmail "app password" (not your normal password)
   - DIGEST_TO           -> the email address to send the digest TO
3. pip install -r requirements.txt
4. python digest.py
"""

import os
import smtplib
import ssl
import time
from datetime import datetime, timedelta, timezone
from email.mime.text import MIMEText

import feedparser
import requests

from config import FEEDS, KEYWORDS, LOOKBACK_DAYS

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"].strip()
SMTP_USER = os.environ["SMTP_USER"].strip()
SMTP_PASS = os.environ["SMTP_PASS"].strip()
DIGEST_TO = os.environ["DIGEST_TO"].strip()

# Routes to whichever free OpenRouter model is available.
OPENROUTER_MODEL = "openrouter/free"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Reddit rate-limits aggressive bots; space out requests and look browser-like.
REDDIT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; AgenticBackendDigest/1.0; "
        "+https://github.com/post_extractor)"
    ),
    "Accept": "application/atom+xml,application/rss+xml,application/xml;q=0.9,*/*;q=0.8",
}
FEED_DELAY_SECONDS = 8


def is_recent(entry, cutoff):
    """Return True if the entry has a publish date within the lookback window."""
    for field in ("published_parsed", "updated_parsed"):
        t = entry.get(field)
        if t:
            published = datetime(*t[:6], tzinfo=timezone.utc)
            return published >= cutoff
    # If no date is available, keep it rather than silently dropping it.
    return True


def is_relevant(entry):
    """Return True if the entry's title/summary mentions any tracked keyword."""
    text = (entry.get("title", "") + " " + entry.get("summary", "")).lower()
    return any(kw.lower() in text for kw in KEYWORDS)


def fetch_feed(url, retries=3):
    """Fetch an RSS URL with retries for Reddit 429 rate limits."""
    last_error = None
    for attempt in range(retries):
        try:
            resp = requests.get(url, headers=REDDIT_HEADERS, timeout=20)
            if resp.status_code == 429:
                wait = FEED_DELAY_SECONDS * (attempt + 2)
                print(f"[warn] rate-limited ({url}); waiting {wait}s then retrying")
                time.sleep(wait)
                last_error = requests.HTTPError(
                    f"429 Too Many Requests for url: {url}", response=resp
                )
                continue
            resp.raise_for_status()
            return resp.content
        except requests.RequestException as e:
            last_error = e
            time.sleep(FEED_DELAY_SECONDS)
    raise last_error


def collect_entries():
    """Pull and filter entries from every feed in config.FEEDS."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)
    collected = []

    for i, (source_name, url) in enumerate(FEEDS.items()):
        if i > 0:
            time.sleep(FEED_DELAY_SECONDS)
        try:
            content = fetch_feed(url)
            parsed = feedparser.parse(content)
        except requests.RequestException as e:
            print(f"[warn] could not fetch feed for {source_name}: {e}")
            continue

        if parsed.bozo and not parsed.entries:
            print(f"[warn] could not parse feed for {source_name}: {url}")
            continue

        for entry in parsed.entries:
            if is_recent(entry, cutoff) and is_relevant(entry):
                collected.append(
                    {
                        "source": source_name,
                        "title": entry.get("title", "(no title)"),
                        "link": entry.get("link", ""),
                        "summary": entry.get("summary", "")[:500],
                    }
                )

    return collected


def build_prompt(entries):
    """Turn the raw entries into a single prompt for the LLM to summarize."""
    if not entries:
        return None

    lines = []
    for e in entries:
        lines.append(f"- [{e['source']}] {e['title']}\n  {e['summary']}\n  {e['link']}")
    raw_content = "\n".join(lines)

    prompt = f"""You are helping me stay on top of agentic AI and backend engineering content.

Below is a raw list of recent posts pulled from accounts I follow (Reddit + X/Twitter feeds).
Please produce a concise digest with:

1. A short "Top picks" section (3-5 items max) highlighting the most substantive/technical posts.
2. Grouped sections by theme (e.g. "Agent frameworks", "Backend/infra", "LLM serving", "Misc"),
   each with 1-2 sentence summaries per item and the source link.
3. Skip anything that's just marketing, low-effort, or purely promotional.
4. Keep the whole digest under 500 words.

Raw posts:
{raw_content}
"""
    return prompt


def summarize_with_openrouter(prompt):
    """Call OpenRouter's free model router to generate the digest summary."""
    if not OPENROUTER_API_KEY:
        raise RuntimeError(
            "OPENROUTER_API_KEY is empty after stripping whitespace. "
            "Re-check the GitHub secret value."
        )

    response = requests.post(
        OPENROUTER_URL,
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/post_extractor",
            "X-Title": "Agentic Backend Digest",
        },
        json={
            "model": OPENROUTER_MODEL,
            "max_tokens": 1200,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=90,
    )
    if not response.ok:
        raise RuntimeError(
            f"OpenRouter API {response.status_code}: {response.text}"
        )

    data = response.json()
    choices = data.get("choices") or []
    if not choices:
        raise RuntimeError(f"OpenRouter returned no choices: {data}")

    content = choices[0].get("message", {}).get("content")
    if not content:
        raise RuntimeError(f"OpenRouter returned empty content: {data}")
    return content


def send_email(subject, body):
    """Send the digest via Gmail SMTP."""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = DIGEST_TO

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, [DIGEST_TO], msg.as_string())


def main():
    entries = collect_entries()
    print(f"Collected {len(entries)} relevant, recent entries.")

    if not entries:
        print("Nothing new to summarize. Exiting without sending an email.")
        return

    prompt = build_prompt(entries)
    summary = summarize_with_openrouter(prompt)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    subject = f"Agentic/Backend Digest — {today}"

    send_email(subject, summary)
    print("Digest sent.")

    # Also write to disk so you have a local record / can commit it in CI.
    with open("digest_latest.md", "w") as f:
        f.write(f"# {subject}\n\n{summary}\n")


if __name__ == "__main__":
    main()
