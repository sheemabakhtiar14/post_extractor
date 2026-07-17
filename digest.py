"""
Agentic/Backend Content Digest
--------------------------------
Pulls recent posts from RSS feeds (Reddit natively, X/Twitter via an RSS
bridge you configure), filters them for relevance + recency, summarizes
them with the Claude API, and emails you the result.

Run this on a schedule (e.g. GitHub Actions, cron) every 2-3 days.

SETUP
1. Fill in FEEDS below with your RSS URLs (see config.py / README).
2. Set these environment variables (as GitHub Actions secrets, or locally):
   - ANTHROPIC_API_KEY   -> your Claude API key
   - SMTP_USER           -> the Gmail address you're sending FROM
   - SMTP_PASS           -> a Gmail "app password" (not your normal password)
   - DIGEST_TO           -> the email address to send the digest TO
3. pip install -r requirements.txt
4. python digest.py
"""

import os
import smtplib
import ssl
from datetime import datetime, timedelta, timezone
from email.mime.text import MIMEText

import feedparser
import requests

from config import FEEDS, KEYWORDS, LOOKBACK_DAYS

ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
SMTP_USER = os.environ["SMTP_USER"]
SMTP_PASS = os.environ["SMTP_PASS"]
DIGEST_TO = os.environ["DIGEST_TO"]

CLAUDE_MODEL = "claude-sonnet-4-6"


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


def collect_entries():
    """Pull and filter entries from every feed in config.FEEDS."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)
    collected = []
    headers = {"User-Agent": "agentic-backend-digest-bot/1.0"}

    for source_name, url in FEEDS.items():
        try:
            resp = requests.get(url, headers=headers, timeout=20)
            resp.raise_for_status()
            parsed = feedparser.parse(resp.content)
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
    """Turn the raw entries into a single prompt for Claude to summarize."""
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


def summarize_with_claude(prompt):
    """Call the Claude API to generate the digest summary."""
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": CLAUDE_MODEL,
            "max_tokens": 1200,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    return "".join(block.get("text", "") for block in data.get("content", []))


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
    summary = summarize_with_claude(prompt)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    subject = f"Agentic/Backend Digest — {today}"

    send_email(subject, summary)
    print("Digest sent.")

    # Also write to disk so you have a local record / can commit it in CI.
    with open("digest_latest.md", "w") as f:
        f.write(f"# {subject}\n\n{summary}\n")


if __name__ == "__main__":
    main()
