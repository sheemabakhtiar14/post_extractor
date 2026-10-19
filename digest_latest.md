# Agentic/Backend Digest — 2026-10-19

**Top picks (5)**  
1. Google open‑sources **Harness2**, a framework for self‑improving AI agents (Reddit).  
2. **DeepSeek‑V4.1‑Flash** reaches 2.61 bpw and ~26 t/s on dual RTX 3090s (Reddit).  
3. A custom inference engine lets a 32 B model run with 262 K context in a 16 GB GPU budget (Reddit).  
4. **ORL** diffusion LLM hits 2,788 tokens/s on a single RTX 5090 (Reddit).  
5. A minimal **IPython harness** ties production coding agents to Qwen‑3.5‑9B, cutting run‑to‑run variance (Reddit).  

**Agent frameworks**  
- **Harness2** (Google) – an open‑source toolkit that lets agents self‑train and iteratively improve their own prompts and code (https://www.reddit.com/r/LocalLLaMA/comments/1x9gfnb/google_open_sources_harness2_for_self_improving/).  
- **Bare IPython harness** – a lightweight loop that connects production‑grade coding agents to Qwen‑3.5‑9B while normalising tool outputs, dramatically reducing variance (https://www.reddit.com/r/LocalLLaMA/comments/1x9vtt9/a_bare_ipython_harness_ties_production_coding/).  

**Backend / infra**  
- **Custom inference engine** – enables a 32 B model to retain 262 K tokens within a 16 GB GPU limit, demonstrated on a single RTX 4090 (https://www.reddit.com/r/LocalLLaMA/comments/1xa02iw/we_built_our_own_inference_engine_so_a_32b_model/).  
- **DeepSeek‑V4.1‑Flash** – runs at 2.61 bpw with ~26 tokens per second on dual RTX 3090s, ideal for fast programming and agent workloads (https://www.reddit.com/r/LocalLLaMA/comments/1x9umtv/deepseek_v41_flash_at_261_bpw_engram_2.6_t_on/).  
- **ORL diffusion LLM** – achieves 2,788 tokens/s on a single RTX 5090, showing diffusion‑based language models can be served at extreme speed (https://www.reddit.com/r/MachineLearning/comments/1x7qgr0/research_2788_tokenss_on_a_single_rtx_5090_with_a/).  

**Miscellaneous technical advances**  
- **Qwen‑3.8‑27B & Flash‑Next** – benchmarked engine performance on dual RTX 5070 Ti (96 GB RAM) reveals cost‑effective inference for consumer‑grade hardware (https://www.reddit.com/r/LocalLLaMA/comments/1x9tzf1/qwen3827b_and_flashnext_on_consumer_hardware/).  
- **Minimax M3.1‑Flash 428 B** – highlights that the 23 billion‑parameter variant exceeds typical 2‑GPU memory caps, underscoring hardware limits for massive models (https://www.reddit.com/r/LocalLLaMA/comments/1x9xc0c/minimax_m31_flash_is_428b_23a/).  
- **Proof‑Before‑Reuse** – shows restricting an agent’s view to only reproduced sessions prevents poisoned skills from entering procedural memory (https://www.reddit.com/r/MachineLearning/comments/1x975ea/proof_before_reuse_showing_agents_only_what_later/).
