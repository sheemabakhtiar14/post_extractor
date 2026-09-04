# Agentic/Backend Digest — 2026-09-04

# Agentic AI & Backend Digest

## Top picks
1. **Paddock inference engine** — Rust/C++ engine with custom CUDA kernels, dual MIT/Apache-2.0 licensing, OpenAI/Anthropic APIs, processes 300B tokens/yr in production.
2. **EvoUndo** — Framework for safely undoing LLM agent self-modifications to prompts/tools/harnesses; addresses a real gap in agent reliability.
3. **MoE expert-budget trick** — Runtime-only router tweak on late layers cuts reasoning tokens 8.5% with zero retraining on Qwen3 35B-A4B+.

---

## Inference / LLM Serving
- **Paddock open-sourced** — Rust/C++ engine, custom CUDA kernels, loads GGUF/safetensors, serves OpenAI + Anthropic-style APIs from one binary. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w6z9oh/we_opensourced_paddock_our_rustc_inference_engine/)
- **Qwen3.8-Flash-Next on 2x3090** — Author pushes decode 25–29 → 37–41 t/s via expert caching + MTP on PCIe 3.0 hardware. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w6ozbj/update_qwen38flashnext_on_2x3090_ddr4_part_2_2529/)
- **MoE active-params optimization** — Expand top-K only in late transformer layers with linear decay; no retraining needed. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w6lk6z/increasing_active_parameters_per_token_in_moe/)
- **TimesFM-3 released** — Google's 330M time-series foundation model with native multivariate forecasting (non-commercial). [link](https://www.reddit.com/r/LocalLLaMA/comments/1w6hlpt/google_released_timesfm3_a_330mparameter_time/)

## Agent Frameworks
- **ARC AGI-3 hype check** — Nvidia's AVO harness already hit 100%, contextualizing GPT-6 Astra's 98.6% claim. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w6z731/on_gpt6_astra_986_arc_agi3_dont_fall_for_the_hype/)
- **EvoUndo (agent self-evolution safety)** — Represents, synthesizes, diagnoses, and verifies recoverability of model-generated harness modifications. [link](https://www.reddit.com/r/MachineLearning/comments/1w4m0hq/evoundo_recoverabilityconstrained_selfevolution/)
- **Latent Reasoning Landscape 2026** — Maps BDH-CQ, HRM/TRM, Coconut as alternative reasoning paths beyond token-stream CoT. [link](https://www.reddit.com/r/MachineLearning/comments/1w4evwo/latent_reasoning_landscape_in_2026_mapping_bdhcq/)

## Research / Methods
- **Deepity (C++ ML lib)** — Predictive Coding Networks hit 97.73% MNIST in 60s via Direct Kolen-Pollack Feedback Alignment. [link](https://www.reddit.com/r/MachineLearning/comments/1w5fuhm/deepity_a_c_library_showing_predictive_coding/)
- **Open-source AI detectors fail FPR test** — At a matched 0.5% FPR on 6,930 human docs, most detectors lose frontier-model detection. [link](https://www.reddit.com/r/MachineLearning/comments/1w58erw/most_opensource_ai_detectors_cant_hold_a_05/)
- **Pilot-based LLM reliability protocol** — Applies generalizability theory to choose repeat counts for stable brand-recommendation comparisons. [link](https://www.reddit.com/r/MachineLearning/comments/1w6wtw7/how_many_repeated_llm_queries_are_enough_testing/)

## Misc
- **JEPA-grounded LLMs** — Discussion on using JEPA world models trained in simulation to give LLMs physical intuition (Mary's Room framing). [link](https://www.reddit.com/r/MachineLearning/comments/1w69gvd/grounding_llms_with_jepabased_world_models/)
- **Translation model prompt adherence** — Gemma 4 and Qwen3.8 still execute reasoning inside translation data; structured decoding helps but isn't bulletproof. [link](https://www.reddit.com/r/LocalLLaMA/comments/1w71vg1/even_qwen38_followed_the_instruction_inside_my/)

*(Self-promo thread, beginner question, AAMAS submission advice, Triton giveaway, and YOLO26 deraining repurposing post omitted as low-signal.)*
