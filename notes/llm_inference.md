# LLM Inference Notes

- Latency is often dominated by KV cache reads and memory bandwidth.
- Memory usage grows with: batch_size × seq_len × num_layers × hidden_size.
- Systems like vLLM use:
  - PagedAttention to virtualize KV cache into pages.
  - Continuous batching to keep the GPU fully utilized.
- Speculative decoding reduces latency by using a small draft model then verifying with a larger model.
- Quantization + optimized attention kernels (e.g., FlashAttention) help trade accuracy for speed.
