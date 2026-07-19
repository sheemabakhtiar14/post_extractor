# Agentic/Backend Digest — 2026-07-19

**Top picks**
- Netflix’s in-house LLM serving writeup (Triton wrapper, full stack) — production infra lessons. https://x.com/m_rasu/status/2078643215780225284
- LMCache for KV-cache reuse: up to 10.7x prefill speedup, 3–10x on AMD MI300X. https://x.com/rohanpaul_ai/status/2077853724555534509
- Thinking Machines’ Tinker result actually used Qwen3-235B; base model choice scrutinized via benchmarks. https://www.reddit.com/r/LocalLLaMA/comments/1v0ka8g/
- Aurora DSQL paper: minimize coordination as core latency-reduction principle. https://x.com/karthikkalyan90/status/2078740157759672643
- LLM harness tool to catch cache invalidation in calls. https://www.reddit.com/r/LocalLLaMA/comments/1uztipo/

**LLM serving / infra**
- Cache hit rate optimization flagged as underrated lever; providers discount cached tokens heavily. https://x.com/saen_dev/status/2078744875466457118
- Stateful routing replacing stateless L7 LB in AI hot path for GPU efficiency. https://x.com/shubh6200/status/2078366054925881502
- Mini-SGLang: 5k-line Python inference framework demystifying serving optimizations. https://x.com/the_osps/status/2078435617898442832
- Position-independent caching (HYPIC) for hybrid-attention RAG/agent serving. https://x.com/locox_fun/status/2077718968455078041
- Multi-provider failover harness open-sourced by Metriqual. https://x.com/its_vayishu/status/2078098851593093444

**Backend / distributed systems**
- Backend architect 2026 skill list: microservices, CAP, event sourcing, CQRS. https://x.com/SumitM_X/status/2078720127227576753
- Uber-at-scale design notes: H3 indexing, Kafka event architecture. https://x.com/Anupkpal9650/status/2078435701780361248
- Production-focused engineering knowledge base repo published. https://x.com/aos_tsx/status/2078585579701518815
- r/ExperiencedDevs: practical NestJS rate-limiting for external API with soft 20 req/s limit. https://www.reddit.com/r/ExperiencedDevs/comments/1uy3m06/

**Agent frameworks / local models**
- ASCIITermDraw Bench: tests VLMs generating/editing ASCII. https://www.reddit.com/r/LocalLLaMA/comments/1v0ltno/
- Qwen 3.6 vs Gemma 4 local: prompt adherence/coherence observations. https://www.reddit.com/r/LocalLLaMA/comments/1v0dksm/
- Fine-tuning ternary Bonsai 8b on Apple metal. https://www.reddit.com/r/LocalLLaMA/comments/1v0egoi/
- Basalt Labs scam: fake 99.44% HLE claim, Qwen2.5-7B under hood. https://www.reddit.com/r/LocalLLaMA/comments/1uztylz/

**Misc**
- r/ExperiencedDevs: joy in SWE when LLMs handle implementation. https://www.reddit.com/r/ExperiencedDevs/comments/1uzfvrq/
- Full local movie gen on M5 Max (flux/wan/ltx/piper). https://www.reddit.com/r/LocalLLaMA/comments/1v0ibu2/
