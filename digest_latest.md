# Agentic/Backend Digest — 2026-07-25

**Top picks (3‑5)**  
- **Inflect v2** – two ultra‑tiny, fully open‑source TTS models (< 4 M and 10 M parameters) that run on a single GPU. https://www.reddit.com/r/LocalLLaMA/comments/1v5ve6v/i_released_inflect_v2_two_ultratiny_complete_tts/  
- **Statistically‑Lossless Quantization** – a paper showing lossless weight quantization for LLMs by preserving statistical distribution properties, shrinking model size without accuracy loss. https://www.reddit.com/r/LocalLLaMA/comments/1v5j35f/paper_statisticallylossless_quantization_of_large/  
- **CachyLLama** – a llama.cpp fork adding a persistent “SSD‑style” KV cache, dramatically cutting latency for long‑running local‑agent sessions. https://www.reddit.com/r/LocalLLaMA/comments/1v5k08a/cachyllamas_llamacpp_fork_with_persistent_kv/  
- **The Stack v3** – Hugging Face’s biggest open‑code dataset to date (> 1 billion lines of permissively licensed code) for training and research. https://www.reddit.com/r/LocalLLaMA/comments/1v59aek/hugging_face_releases_the_stack_v3_largest_open/  
- **Compiler‑to‑weights** – a tool that compiles a Python computation graph into a ready‑to‑load vanilla transformer checkpoint, requiring no training. https://www.reddit.com/r/MachineLearning/comments/1v5fxbe/i_built_a_compiler_that_turns_computation_graphs/  

---

### Agent frameworks
- **CachyLLama** – persistent KV‑cache reduces per‑token latency for multi‑turn local agents on modest hardware. https://www.reddit.com/r/LocalLLaMA/comments/1v5k08a/cachyllamas_llamacpp_fork_with_persistent_kv/  
- **DKV** – open‑source KV‑cache compression framework with CLI tools and a technical report reporting up to 4× size reduction. https://www.reddit.com/r/LocalLLaMA/comments/1v5wviz/dkv_opensource_kvcache_compression_framework_for/  

### Backend / infrastructure
- **Inflect v2** – tiny TTS models enable edge‑device deployment of voice assistants at low cost. https://www.reddit.com/r/LocalLLaMA/comments/1v5ve6v/i_released_inflect_v2_two_ultratiny_complete_tts/  
- **The Stack v3** – massive, diversified code corpus accelerates training of code‑oriented models. https://www.reddit.com/r/LocalLLaMA/comments/1v59aek/hugging_face_releases_the_stack_v3_largest_open/  
- **Compiler‑to‑weights** – emits a standard transformer checkpoint directly from a computation graph, eliminating any training pipeline. https://www.reddit.com/r/MachineLearning/comments/1v5fxbe/i_built_a_compiler_that_turns_computation_graphs/  
- **Intel consumer platforms (Z890)** – lack adequate PCIe bifurcation for peer‑to‑peer GPU traffic, making them poor choices for multi‑GPU AI workloads. https://www.reddit.com/r/LocalLLaMA/comments/1v5x1h0/psa_do_not_use_intel_consumer_platforms_for/  

### LLM serving
- **Statistically‑Lossless Quantization** – enables true lossless quantization of LLMs, preserving fidelity while shrinking model size for efficient serving. https://www.reddit.com/r/LocalLLaMA/comments/1v5j35f/paper_statisticallylossless_quantization_of_large/  

### Miscellaneous
- **The Stack v3** (also valuable as a research resource) – the largest open‑code dataset to date, useful for pretraining and benchmarking. https://www.reddit.com/r/LocalLLaMA/comments/1v59aek/hugging_face_releases_the_stack_v3_largest_open/
