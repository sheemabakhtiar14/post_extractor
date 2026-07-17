"""
Edit this file to control which sources get pulled and what counts as
'relevant' content. No need to touch digest.py for normal tweaks.
"""

# --- FEEDS ---------------------------------------------------------------
# Reddit RSS is native and free: https://www.reddit.com/r/<subreddit>/.rss
#
# X topic search: public RSSHub keyword feeds are currently broken (404).
# To get X topic coverage, create search feeds on https://rss.app :
#   1. Create feed → paste an X search URL, e.g.
#        https://x.com/search?q=agentic%20OR%20%22AI%20agents%22&f=live
#   2. Copy the generated RSS URL into FEEDS below (replace the placeholders).
#
# Add/remove entries freely. Key = label shown in the digest, value = RSS URL.

FEEDS = {
    # Reddit (native RSS, no setup needed)
    "r/LocalLLaMA": "https://www.reddit.com/r/LocalLLaMA/.rss",
    "r/MachineLearning": "https://www.reddit.com/r/MachineLearning/.rss",
    "r/ExperiencedDevs": "https://www.reddit.com/r/ExperiencedDevs/.rss",

    # X — topic search via rss.app
    "x:LLM infra/serving": "https://rss.app/feeds/IxhdYZp2PG0zT99e.xml",
    "x:distributed systems": "https://rss.app/feeds/JJeBllQRg3jgTsKl.xml",
}

# --- KEYWORDS --------------------------------------------------------------
# A post is kept if its title or summary contains ANY of these (case-insensitive).
# Tuned for agentic workflows, agents, backend, infra, and systems.

KEYWORDS = [
    # Agents / agentic workflows
    "agent", "agents", "agentic", "workflow", "workflows",
    "multi-agent", "orchestration", "tool calling", "tool use",
    "MCP", "autonomous", "planner", "planning",

    # LLMs / RAG / serving
    "LLM", "RAG", "inference", "serving", "evals", "evaluation",

    # Backend / infra / systems
    "backend", "infra", "infrastructure", "systems",
    "distributed systems", "distributed", "architecture",
    "pipeline", "pipelines", "scalability", "scaling",
    "observability", "reliability", "production",
]

# --- LOOKBACK WINDOW ---------------------------------------------------------
# How many days back to pull. Set to match how often you run the job.
LOOKBACK_DAYS = 3
