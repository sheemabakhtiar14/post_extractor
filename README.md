# Agentic/Backend Content Digest

Pulls recent posts from RSS feeds (Reddit natively, X via a bridge you
configure), filters for relevance, summarizes with Claude, and emails you
the result every 2-3 days — for free.

## Files
- `digest.py` — main script: fetch → filter → summarize → email
- `config.py` — edit this to add/remove feeds and keywords
- `requirements.txt` — Python dependencies
- `digest.yml` — GitHub Actions workflow (move to `.github/workflows/digest.yml`)

## Setup (10-15 min)

### 1. Create a repo
Create a new **private** GitHub repo and put all these files in it.
Move `digest.yml` into `.github/workflows/digest.yml`.

### 2. Get a Claude API key
Sign up at console.anthropic.com and create an API key. New accounts get
free credits, and this workload (one summarization call every 2-3 days,
processing maybe 20-40 short posts) is small — it should cost cents per
run even after any free credits run out.

### 3. Set up a Gmail app password (free)
- Go to your Google Account → Security → 2-Step Verification (must be on)
- Go to "App passwords" → generate one for "Mail"
- Save the 16-character password — this is `SMTP_PASS`, NOT your normal
  Gmail password.

### 4. Add GitHub Secrets
In your repo: Settings → Secrets and variables → Actions → New repository secret.
Add:
| Secret name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | your Claude API key |
| `SMTP_USER` | your Gmail address |
| `SMTP_PASS` | the app password from step 3 |
| `DIGEST_TO` | the email address you want the digest sent to (can be the same Gmail) |

### 5. Set up your feeds
Open `config.py`:
- **Reddit** feeds work immediately — no setup needed.
- **X/Twitter** feeds need an RSS bridge since X has no free official RSS.
  Options, easiest first:
  - **rss.app** — free tier, generate an RSS URL per X account, paste it in
  - **RSSHub** — free, more feeds, but the public instance (`rsshub.app`) can
    be rate-limited; self-hosting is more reliable if you want to go that route
  - Skip X entirely at first and get the pipeline working with Reddit only —
    add X feeds once the rest works.

### 6. Test it locally (optional but recommended)
```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
export SMTP_USER=you@gmail.com
export SMTP_PASS=your16charapppassword
export DIGEST_TO=you@gmail.com
python digest.py
```
You should get an email within a few seconds, and a `digest_latest.md`
file will be written locally.

### 7. Turn on the schedule
Once the secrets are set and you've pushed the workflow file, GitHub
Actions will run it automatically every 3 days. You can also trigger it
manually anytime from the repo's "Actions" tab → "content-digest" →
"Run workflow".

## Tuning
- **Too many/too few results?** Edit `KEYWORDS` in `config.py`.
- **Change frequency?** Edit the `cron` line in `digest.yml`
  (e.g. `0 9 */2 * *` for every 2 days).
- **Want it grouped differently?** Edit the summarization instructions
  inside `build_prompt()` in `digest.py`.

## Known limitations
- X/Twitter has no free official read API — this relies on third-party RSS
  bridges, which can occasionally break or rate-limit. Treat X coverage as
  a bonus layer on top of a reliable Reddit core, not a guarantee.
- LinkedIn has no practical free automation route and isn't included here.
- The Claude API is technically a paid service, but at this volume
  (one call every 2-3 days) cost is negligible.
