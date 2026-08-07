# Agentic/Backend Digest — 2026-08-07

**Top picks**

1. **C++ vLLM port** – 66 MiB binary, no Python at inference, token-for-token parity with vLLM.  
2. **NVIDIA NeMo-Speech.cpp** – Full ASR/TTS/codec stack quantized to GGUF, fully on-device.  
3. **Monodratic** – Sparse causal attention via learned product-hash routing; claims efficiency gains.  

---

**Agents & Frameworks**  
- **Qwen 3.8 Max tops agentic index**, beating Opus 5 per Artificial Analysis. [Link](https://www.reddit.com/r/LocalLLaMA/comments/1vhd416/qwen_38_max_now_ranked_as_best_overall_model/)  
- **Criticism of AA's weighting changes** after open-source lead, suggesting bias via metric tuning. [Link](https://www.reddit.com/r/LocalLLaMA/comments/1vhoyw1/my_issue_with_artificial_analysiss_intelligence/)  

**Backend/Infra**  
- **AMD acquires Taalas**, aiming to scale AI inference compute, possibly eyeing modular chip designs. [Link](https://www.reddit.com/r/LocalLLaMA/comments/1vhrdo3/amd_acquires_taalas_to_advance_compute_solutions/)  
- **Dual 3090 setup hits 1600 pp/t** on Qwen 3.6 27B with `--split-mode tensor`. [Link](https://www.reddit.com/r/LocalLLaMA/comments/1vhkln6/dual_3090_setup_400_pp_ts_to_1600_pp_ts_on_qwen/)  

**LLM Serving**  
- **vLLM ported to C++20**, tiny binary, verified output match—potential edge deployment win. [Link](https://www.reddit.com/r/LocalLLaMA/comments/1vh9lx4/i_ported_vllms_serving_stack_to_c20_66_mib_binary/)  
- **Echo Dot 2 runs 28M LLM** locally with usable speed—low-cost inference hack. [Link](https://www.reddit.com/r/LocalLLaMA/comments/1vhocl8/echo_dot_2_can_run_28m_llm_at_decent_speed/)  

**Speech/NLP Tooling**  
- **NeMo-Speech.cpp enables local ASR+TTS+codec**, all GGUF quantized. [Link](https://www.reddit.com/r/LocalLLaMA/comments/1vhjeqy/nvidias_whole_speech_stack_just_went_local_asr/)  
- **Nemotron 3.5 ASR powers Pi voice extension**, CPU-realtime STT. [Link](https://www.reddit.com/r/LocalLLaMA/comments/1vhvblg/i_made_a_simple_local_voice_input_extension_for/)  

**Research Trends**  
- **Bad Apple compressed into 3MB NN**, SIREN-based method revisited. [Link](https://www.reddit.com/r/MachineLearning/comments/1vfrco1/i_compressed_bad_apple_into_a_3mb_neural_network_p/)  
- **Debate: Can LLM traces become deterministic pipelines?** Examines automation trade-offs. [Link](https://www.reddit.com/r/MachineLearning/comments/1vhapso/can_recurring_llm_traces_be_synthesized_into/)  
- **LLMs may level research playing field**—boosts output for small teams sans mentorship. [Link](https://www.reddit.com/r/MachineLearning/comments/1vgh075/do_llms_make_ml_research_more_fair_for_small/)  

**Hardware**  
- **Custom quad 7900 XTX watercool build**, 96GB VRAM for heavy inference. [Link](https://www.reddit.com/r/LocalLLaMA/comments/1vhs70b/custom_water_cooled_quad_7900_xtx_build_96_gb_vram/)  

**Misc**  
- **Supermarket sells preloaded LLMs**—marketing or real trend? [Link](https://www.reddit.com/r/LocalLLaMA/comments/1vgj0h8/you_can_now_buy_llms_at_your_local_supermarket/)
