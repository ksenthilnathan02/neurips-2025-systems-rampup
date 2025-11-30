# KV Cache Notes

- KV cache stores key/value tensors for each layer and each generated token.
- Rough memory formula:
  - memory ≈ batch × seq_len × num_layers × 2 (K+V) × hidden_size × bytes_per_param.
- Long context and large batch sizes quickly make KV cache the main memory cost.
- Optimization directions:
  - KV compression (low-rank, quantization).
  - Sparse or chunked attention.
  - Paged/virtualized KV (like vLLM's PagedAttention).
  - Offloading KV to CPU/disk with smart prefetching.
