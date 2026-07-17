"""
Edit this file to control which sources get pulled and what counts as
'relevant' content. No need to touch digest.py for normal tweaks.
"""

# --- FEEDS ---------------------------------------------------------------
# Reddit RSS is native and free: https://www.reddit.com/r/<subreddit>/.rss
#
# X topic search (not accounts): RSSHub keyword feeds
#   https://rsshub.app/twitter/keyword/<topic>
# Public RSSHub often rate-limits or needs auth for X — treat as best-effort.
# More reliable alternative: create keyword/search feeds on rss.app and paste URLs here.
#
# Add/remove entries freely. Key = label shown in the digest, value = RSS URL.

FEEDS = {
    # Reddit (native RSS, no setup needed)
    "r/LocalLLaMA": "https://www.reddit.com/r/LocalLLaMA/.rss",
    "r/MachineLearning": "https://www.reddit.com/r/MachineLearning/.rss",
    "r/ExperiencedDevs": "https://www.reddit.com/r/ExperiencedDevs/.rss",

    # X — topic keyword search (not specific accounts)
    "x:agentic": "https://rsshub.app/twitter/keyword/agentic",
    "x:AI agents": "https://rsshub.app/twitter/keyword/AI%20agents",
    "x:agentic workflows": "https://rsshub.app/twitter/keyword/agentic%20workflows",
    "x:multi-agent": "https://rsshub.app/twitter/keyword/multi-agent",
    "x:MCP": "https://rsshub.app/twitter/keyword/MCP",
    "x:LLM infra": "https://rsshub.app/twitter/keyword/LLM%20infrastructure",
    "x:backend systems": "https://rsshub.app/twitter/keyword/backend%20systems",
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
