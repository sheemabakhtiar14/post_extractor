# Agentic/Backend Digest — 2026-10-31

**Top Picks**
1. **Lawyer with GPUs Pt. 3: DeepSeek-V4.1-Flash on 2× DGX Spark** – Exhaustive benchmark (2,600+ tok/s prefill, 322 tok/s structured decode) with full stack details and raw data; run via Claude Code.  
2. **Qwen3.8-Flash-Next on 2× RTX 5090: QEngine 1.3.1 deep-dive** – 504 tok/s decode; 1.5–1.9× speedup vs. next-best engine, with caveats on context length & quantization artifacts.  
3. **TKintegers K5: Balanced-ternary weights beat TorchAO FP8 on L4** – 3.2× prefill / 3.1× decode throughput despite no native K5 HW support; novel GPU kernel design.  
4. **Arc: 70 MB streaming ASR+NLU in one model** – Single model emits transcripts, linked entities, numbers, speaker roles, and audio events every 100 ms.  
5. **vLLM nightly adds PLE disk offload** – Page-Layer Eviction lets KV cache spill to NVMe, enabling longer contexts on limited VRAM.

---

### LLM Inference & Serving
- **vLLM PLE disk offload (nightly)** – KV cache pages evicted to disk transparently; reduces OOM on long-context workloads.  
  https://www.reddit.com/r/LocalLLaMA/comments/1xjpbcg/vllm_now_has_ple_disk_offload_support
