# Scaling Laws Notes

- Scaling laws relate:
  - Model size (parameters),
  - Dataset size (tokens),
  - Compute (FLOPs),
  - Performance (loss / accuracy).
- Chinchilla-style result:
  - Many large models were undertrained for their size.
  - For a fixed compute budget, there is an optimal model size vs token count.
- Practical impact:
  - Don't just keep increasing parameters without enough data.
  - Distillation + quantization are key for deployment efficiency.
