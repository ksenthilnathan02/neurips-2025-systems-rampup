# 🚀 NeurIPS 2025 — AI/ML Systems Ramp-Up

This repository is my structured, 48-hour learning ramp-up focused on the core AI/ML systems topics that are most relevant for NeurIPS 2025 recruiting and technical discussions.  
It contains **lightweight code demos + concise technical notes** covering the essentials of:

- ⚡ **LLM Inference Systems** (vLLM concepts, PagedAttention, batching)
- 🧠 **KV Cache Internals** + memory estimation script
- 🤖 **Agentic Workflows** (LangGraph-style stateful pipelines)
- 🖼️ **Multimodal Models** (VLM fundamentals: CLIP, SigLIP, LLaVA)
- 🔍 **RAG Pipelines** (tiny example with FAISS + sentence-transformers)
- 📈 **Scaling Laws** (Chinchilla compute-optimal training basics)
- 🧪 **Evaluations** (MMLU, MMMU, agent evals, tool correctness)

The goal is to demonstrate fluency across modern ML systems, prepare for conversations with researchers & applied scientists at NeurIPS, and show hands-on initiative through well-organized proof-of-work.

---
## 📁 Repository Structure

```text
neurips-2025-systems-rampup/
│
├── agents/
│   └── research_agent.py                 # A simple LangGraph-style research pipeline
│
├── inference/
│   └── kv_cache_memory_estimator.py      # KV cache size calculator
│
├── rag/
│   └── tiny_rag_pipeline.py              # Mini RAG demo with FAISS
│
├── notes/                                # Concise notes for rapid ramp-up
│   ├── llm_inference.md
│   ├── kv_cache_notes.md
│   ├── agent_systems.md
│   ├── multimodal_basics.md
│   ├── scaling_laws.md
│   └── evals_summary.md
│
└── README.md
```



---

## 🎯 Purpose

This project is meant to:

- Build strong *systems intuition* across high-impact LLM topics  
- Enable confident conversations with NeurIPS recruiting teams  
- Serve as a quick reference for LLM inference, memory, agents, RAG, and multimodality  
- Showcase proactive learning through clean examples and organized notes  

Even small, clear demos can have a big impact when networking with researchers or hiring managers.

---

## 🧩 Topics Covered (Short Summaries)

### **1. LLM Inference (vLLM concepts)**
- KV cache is the main memory bottleneck  
- PagedAttention = virtualized KV storage for efficient batching  
- Continuous batching increases GPU utilization  
- Speculative decoding improves latency  

---

### **2. KV Cache Memory Estimation**
Includes a script that approximates memory usage:

memory ≈ batch_size × seq_len × num_layers × 2 × hidden_size × bytes


Useful for discussing throughput, batching, and long-context limits.

---

### **3. Agentic Systems**
- Graph-style control flow (LangGraph-inspired)
- Pipeline for summarization → insight extraction → question generation
- Focus on reliability, planning, and tool correctness

---

### **4. Multimodal Models**
- Vision encoder (CLIP/SigLIP) + language decoder  
- Image embeddings → projected into LM token space  
- Training requires alignment + instruction tuning  

---

### **5. RAG Pipeline**
A minimal working RAG example using:

- Sentence-transformer embeddings  
- FAISS nearest-neighbor search  
- Simple retrieval wrapper  

---

### **6. Scaling Laws**
- Chinchilla: compute-optimal model size vs training tokens  
- Many large models are undertrained for their size  
- Motivates distillation + smaller optimized models  

---

### **7. Evaluations**
- MMLU, GSM8K, HELM for text  
- MMBench, MMMU for multimodal  
- Agent evals must test *multi-step reasoning* + *tool correctness*  

---

## 🛠️ Setup (Optional)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # if you add one
Or install packages manually (transformers, faiss-cpu, sentence-transformers).
```
---

👩‍💻 Author

Keerthana Senthilnathan
M.S. Data Science @ UC San Diego

---

🌟 Notes

This repository represents a fast but focused systems ramp-up, not a deep research repo.
It is meant to show:

- Systems awareness

- Curiosity

- Ability to learn quickly

- Ability to organize technical information

- Genuine interest in ML systems

- Perfect for NeurIPS networking.


---
