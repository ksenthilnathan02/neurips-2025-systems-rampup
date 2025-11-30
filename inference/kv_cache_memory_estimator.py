import math

def kv_cache_bytes(
    num_layers: int,
    hidden_size: int,
    seq_len: int,
    batch_size: int,
    dtype_bytes: int = 2,  # float16/bfloat16
    num_kv_heads: int | None = None,
    num_attention_heads: int | None = None,
) -> int:
    """
    Simple KV cache size estimate:
    size ≈ batch * seq_len * num_layers * 2 (K+V) * hidden_size * bytes_per_param
    If num_kv_heads is provided, we can be slightly more precise.
    """
    if num_kv_heads is not None and num_attention_heads is not None:
        head_dim = hidden_size // num_attention_heads
        per_token = num_kv_heads * head_dim * 2 * dtype_bytes
    else:
        per_token = hidden_size * 2 * dtype_bytes

    return batch_size * seq_len * num_layers * per_token

def human_readable_bytes(n: int) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024:
            return f"{n:.2f} {unit}"
        n /= 1024
    return f"{n:.2f} PB"

if __name__ == "__main__":
    # Example: 32 layers, 4096 hidden, seq_len=4096, batch=8
    num_layers = 32
    hidden_size = 4096
    seq_len = 4096
    batch = 8

    size_bytes = kv_cache_bytes(num_layers, hidden_size, seq_len, batch)
    print("Estimated KV cache:", human_readable_bytes(size_bytes))
