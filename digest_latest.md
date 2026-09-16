# Agentic/Backend Digest — 2026-09-16

**Top picks (4 items)**  
- Qwen3.8‑Flash‑Next can offload most of its KV cache to RAM, running 1 M‑token contexts on three RTX 3090s at ~60 tok/s (Reddit). https://www.reddit.com/r/LocalLLaMA/comments/1whx5xi/you_can_offload_most_of_qwen38flashnexts_kv_cache/  
- SHADOW‑50M, a 44 M‑parameter quantized LLM trained from scratch on 45 B tokens, fits in 19.8 MB and delivers ~1,900 tok/s on CPU (MachineLearning). https://www.reddit.com/r/MachineLearning/comments/1wgzpli/i_trained_a_44m_parameter_quantized_llm_from/  
- LARA provides composable “behaviour” modules that can be attached to frozen LLMs for reasoning, tool use, and retrieval without fine‑tuning (MachineLearning). https://github.com/pfekin/LARA  
- GPU planning for 27 B models: a 48 GB Pro5000 may replace an A40 for faster inference, but selling the A40 is uncertain (Reddit). https://www.reddit.com/r/LocalLLaMA/comments/1whx9mu/what_would_you_do_with_this_mess_of_gpus/  

**Agent frameworks**  
- **LARA** – modular behaviour components for frozen LLMs, enabling reasoning and tool use without fine‑tuning. https://github.com/pfekin/LARA  

**Backend / infra**  
- **GPU strategy** – evaluating a 48 GB Pro5000 to accelerate 27 B inference versus keeping an A40, weighing cost and performance. https://www.reddit.com/r/LocalLLaMA/comments/1whx9mu/what_would_you_do_with_this_mess_of_gpus/  

**LLM serving**  
- **Qwen3.8‑Flash‑Next KV‑cache offload** – moves most KV data to system RAM, allowing 1 M‑token contexts with only a modest speed drop on consumer GPUs. https://www.reddit.com/r/LocalLLaMA/comments/1whx5xi/you_can_offload_most_of_qwen38flashnexts_kv_cache/  
- **Ministral 3 3B on a Galaxy S21** – shows a 3‑billion‑parameter model running efficiently on a phone, demonstrating strong edge‑device inference. https://www.reddit.com/r/LocalLLaMA/comments/1whtcp0/ministral_3_3b_on_a_galaxy_s21_relayed_a/  

**Misc**  
- **GIMP + llama.cpp integration** – a 35 B Qwen model hooked to GIMP via MCP tools produces a first‑attempt flower drawing, highlighting creative local‑model use cases. https://www.reddit.com/r/LocalLLaMA/comments/1whjqv6/connected_a_local_model/
