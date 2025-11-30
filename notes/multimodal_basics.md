# Multimodal Models Notes

- Vision-language models (VLMs) combine:
  - A vision encoder (e.g., CLIP, SigLIP).
  - A language model (e.g., LLaMA-style decoder).
- Images are turned into embeddings, then projected into the LM's token space.
- Training recipe:
  - Pretrain on image–text pairs (captioning, contrastive learning).
  - Instruction-tune with multimodal prompts (e.g., "Describe this chart").
- Challenges:
  - Efficient high-resolution processing.
  - Grounding and precise localization.
  - Robust evaluation across many tasks (VQA, math, charts, documents).
