# Agentic/Backend Digest — 2026-09-07

# Agentic AI & Backend Digest

## Top Picks
1. **KV cache as an agent runtime** — Yandex Research treats the KV-cache itself as interactive agent state, a substantive architectural alternative to standard turn-based chat loops. [link](https://research.yandex.com/blog/the-kv-cache-as-an-agent-runtime)
2. **Language Models Can Control Their Own Attention** — Paper enabling LLMs to self-route attention, potentially eliminating expensive proxy-scoring token pre-selection for long-context retrieval. [link](https://www.reddit.com/r/MachineLearning/comments/1w7sgf3/language_models_can_control_their_own_attention_r/)
3. **Measuring LLM performance drift: 31,352 repeated benchmarks** — Empirical methodology showing API-served models silently shift behavior over time, undermining snapshot-style leaderboards. [link](https://www.reddit.com/r/MachineLearning/comments/1w9llr4/measuring_llm_performance_drift_observations_and/)
4. **EVIE-8B / EVIE-4.5B (Tencent)** — Open weights for high-capacity visual document retrieval, useful for RAG over PDFs and scanned docs. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w9nphc/tencentevie8b_and_evie45b_highcapacity_visual/)
5. **LLM benchmark harness with per-question answer browsing** — Tool for side-by-side qualitative comparison beyond aggregate scores. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w9ad9q/i_built_an_llm_benchmark_harness_that_lets_you/)

## Agent Frameworks & Memory
- **Coding benchmarks that showcase deep capability** — Survey of harder SE evals (Program-Bench, repo-level tasks) that go past Terminal-Bench/LiveCodeBench saturation. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w8us6t/coding_benchmarks_that_are_quickly_showcasing/)
- **Memory graph design — is it overfitting?** — Practitioner discussion of extracting people/events/relations from LoCoMo-style multi-session data without leaking QA pairs into extractors. [link](https://www.reddit.com/r/MachineLearning/comments/1w8ph8b/is_designing_a_memory_graph_around_known_data/)

## LLM Serving / Local Inference
- **DeepSeek-V4-Flash-Vision vs Qwen3.8-Flash-Next at Q8** — Hands-on comparison on dual Strix Halo (RPC llama.cpp); DS-V4FV ~40% slower than Q38FN at same quant. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w96xoi/deepseekv4flashvision_q8_vs_qwen38flashnext_q8/)
- **8 uncensored Qwen 3.8 27B variants benchmarked** — 167 GPU-hours comparing abliterated checkpoints via KL divergence and 13 benchmarks to verify they're actually uncensored. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w8vx6w/8_uncensored_qwen_38_27b_variants_one_base_167/)
- **2× R9700 + 64GB DDR5 running vLLM Radiance/R9V** — Real-world consumer-AMD multi-GPU inference setup report. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w92x3j/2x_r9700_64_gb_ddr5_is_an_absolute_beast_machine/)
- **Local Copilot with VS Code + Lemonade** — Lightweight guide for running local coding assistants without cloud dependencies. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w9puz3/easy_local_copilot_with_vs_code_and_lemonade/)

## Backend / Infra / SRE
- **Stateful stream processing in banking** — Practitioner thread on Flink + Kafka pattern-matching anomaly detection; covers state design, exactly-once semantics, and testing strategies. [link](https://www.reddit.com/r/ExperiencedDevs/comments/1w8ujoj/how_stateful_stream_processing_system_is_actually/)
- **Infra/SRE feeling stuck without k8s** — Career advice thread; relevant for engineers pivoting into platform roles. [link](https://www.reddit.com/r/ExperiencedDevs/comments/1w8emm2/infraplatformsre_background_feeling_stuck_without/)

## Misc / Worth a Look
- **GPT-6 jailbroken in 24h via TIP attack** — Combination of Task-in-Prompt injection with four auxiliary techniques bypasses Astra safety quickly after launch. [link](https://www.reddit.com/r/MachineLearning/comments/1w89m36/gpt6_reportedly_jailbroken_within_24_hours_using/)
- **9 steps: llama.cpp + FreeCAD + pi coding agent → 3D-printable objects** — End-to-end local-agent CAD pipeline generating manufacturable parts. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w9r73k/9_easy_steps_for_llamacpp_a_local_model_freecad/)

*Skipped: low-effort hardware Qs, calorie benchmark (narrow scope), radar classification, PINNStudio, productivity commentary.*
