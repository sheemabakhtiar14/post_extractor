# Agentic/Backend Digest — 2026-08-16

**Top picks**

1. Qwen 3.8 27B abliterated FP8 drastically cuts refusals (64–99%→0–6%) with negligible MMLU/GSM8K drop [Post](https://www.reddit.com/r/LocalLLaMA/comments/1vppox6/qwen3827b_abliterated_fp8_refusal_6499_06_and/)  
2. Jacobian lens from Qwen3.6-27B steers Qwen3.8-27B with no refitting [Post](https://www.reddit.com/r/MachineLearning/comments/1vpa5cv/survival_of_the_fitted_qwen3627bs_jacobian_lens/)  
3. Linear attention recall benchmark problem for 1M-token DNA sequences [Post](https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/)  
4. Apple Silicon inference deep dive with actionable configs [Post](https://www.reddit.com/r/LocalLLaMA/comments/1vphr8u/sota_apple_silicon_inference_august_15_2026/)  
5. torch-preflight catches PyTorch autograd/GPU-hour bugs early [Post](https://www.reddit.com/r/MachineLearning/comments/1vo8vv0/a_linter_for_pytorch_torchpreflight_p/)  

**Agent frameworks / harnesses**  
- **Agentic harness for small models**: user seeks lightweight web RAG + shell + MCP for sub-30B setups [Post](https://www.reddit.com/r/LocalLLaMA/comments/1vpcj2j/agentic_harness_for_small_models/)  
- **llama.cpp Windows Manager**: GUI/utility to manage local llama.cpp backends on Windows [Post](https://www.reddit.com/r/LocalLLaMA/comments/1vpfrxw/llamacpp_windows_manager/)  
- **Qwen3.8 27B in vLLM**: users report excessive “thinking” latency even at low budgets; tuning `max_tokens`, `temperature`, and draft-model decoding suggested [Post](https://www.reddit.com/r/LocalLLaMA/comments/1vpotfv/anyone_managed_to_get_qwen_38_27b_running/)  

**Backend / infra**  
- **RTX 5060 Ti presets**: rebuilt repo focuses on copy-paste configs + high-context harness for consumer GPUs [Post](https://www.reddit.com/r/LocalLLaMA/comments/1vper67/club5060ti_refresh_tested_rtx_5060_ti_presets_a/)  
- **Intel Arc B140 build**: 10-core Xeon + 64GB ECC for ~3-slot local inference box [Post](https://www.reddit.com/r/LocalLLaMA/comments/1vpkomt/showoff_saturday_intel_arc_b140_build/)  
- **Hardware reach**: Qwen 3.8 27B hit 1M downloads but <1000 users on 24GB cards—memory wall is real [Post](https://www.reddit.com/r/LocalLLaMA/comments/1vpm70f/how_many_people_have_24gb_over_gpu_here/)  
- **Linux vs Windows on RTX 5090**: consensus favors Linux/vLLM for throughput >50GB VRAM [Post](https://www.reddit.com/r/LocalLLaMA/comments/1vpncov/5090_windows_or_linux_for_qwen3827b/)  

**LLM serving / optimization**  
- **Gemma 4 E4B IQ2_XXS** gains +140% reasoning via tensor-level quantization allocation [Post](https://www.reddit.com/r/LocalLLaMA/comments/1vp2x49/gemma_4_e4b_iq2_xxs_14054_reasoning_performance/)  
- **LittleLearner** trains LMs on filtered K-12 curriculum vs unfiltered controls—probing what scaling/SFT/ICL amplify [Post](https://www.reddit.com/r/LocalLLaMA/comments/1vpsavl/littlelearner_language_models_under/)  
- **Qwen3.8 vs 3.6 ray-tracing in BASIC**: quirky eval showing instruction-following gap [Post](https://www.reddit.com/r/LocalLLaMA/comments/1vpiyj9/qwen3827b_vs_qwen3627b_writing_raytracers_in_basic/)  

**Research / misc tools**  
- **BDH-CQ**: recurrent latent reasoning boosts in-context learning over vanilla attention [Post](https://www.reddit.com/r/MachineLearning/comments/1vov5r5/bdhcq_incontext_learning_with_recurrent_latent/)  
- **Worldproof**: diagnostic toolkit flagging pixel-metric blind-spots in video-world models [Post](https://www.reddit.com/r/MachineLearning/comments/1vnliv7/worldproof_diagnosing_where_worldmodel/)  
- **City2Graph**: PyTorch lib for heterogeneous GNNs on urban spatial data [Post](https://www.reddit.com/r/MachineLearning/comments/1vn8oya/city2graph_a_python_library_for_heterogeneous/)  
- **RegressionGuard**: anomaly detection for perf regressions via hardware counters, LOO thresholding [Post](https://www.reddit.com/r/MachineLearning/comments/1vngjmv/urgent_help_detecting_performance_regressions/)  
- **ASCII diffusion project**: community feedback requested on
