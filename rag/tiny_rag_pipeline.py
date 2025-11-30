from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Tiny corpus
DOCS = [
    "NeurIPS is a top conference in machine learning.",
    "LLM inference performance is often limited by KV cache memory bandwidth.",
    "Agentic systems combine LLMs with tools, memory, and planning.",
    "Multimodal models process both images and text together."
]

def build_index(docs):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(docs, convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return model, index

def retrieve(query, model, index, k=2):
    q_emb = model.encode([query], convert_to_numpy=True)
    D, I = index.search(q_emb, k)
    return [DOCS[i] for i in I[0]]

if __name__ == "__main__":
    model, index = build_index(DOCS)
    query = "What limits LLM inference speed?"
    results = retrieve(query, model, index, k=2)
    print("Query:", query)
    print("Top docs:")
    for r in results:
        print("-", r)
