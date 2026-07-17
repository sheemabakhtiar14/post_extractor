"""
Edit this file to control which sources get pulled and what counts as
'relevant' content. No need to touch digest.py for normal tweaks.
"""

# --- FEEDS ---------------------------------------------------------------
# Reddit RSS is native and free: https://www.reddit.com/r/<subreddit>/.rss
#
# X/Twitter has no free official RSS. Use a bridge service to generate an
# RSS URL for a specific account, e.g.:
#   - rss.app          (free tier: a handful of feeds)
#   - RSSHub (self-hosted or public instance, e.g. rsshub.app/twitter/user/<handle>)
#   - Nitter instances  (unofficial, often unreliable/rate-limited — treat as bonus, not core)
#
# Add/remove entries freely. Key = label shown in the digest, value = RSS URL.

FEEDS = {
    # Reddit (native RSS, no setup needed)
    "r/LocalLLaMA": "https://www.reddit.com/r/LocalLLaMA/.rss",
    "r/MachineLearning": "https://www.reddit.com/r/MachineLearning/.rss",
    "r/ExperiencedDevs": "https://www.reddit.com/r/ExperiencedDevs/.rss",

    # X/Twitter accounts (replace with your own RSS-bridge URLs)
    # "karpathy": "https://rsshub.app/twitter/user/karpathy",
    # "simonw": "https://rsshub.app/twitter/user/simonw",
    # "hwchase17": "https://rsshub.app/twitter/user/hwchase17",
}

# --- KEYWORDS --------------------------------------------------------------
# A post is kept if its title or summary contains ANY of these (case-insensitive).
# Keep this list reasonably broad — too narrow and you'll get empty digests.

KEYWORDS = [
    "agent", "agentic", "backend", "infra", "infrastructure",
    "LLM", "orchestration", "distributed systems", "API",
    "RAG", "inference", "serving", "observability", "scaling",
    "production", "pipeline", "architecture", "MCP",
]

# --- LOOKBACK WINDOW ---------------------------------------------------------
# How many days back to pull. Set to match how often you run the job.
LOOKBACK_DAYS = 3
