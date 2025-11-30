"""
Toy 'research agent' that:
1. Takes an abstract string.
2. Produces a summary.
3. Extracts key insights.
4. Generates follow-up questions.

We keep the 'LLM' as a placeholder so it runs everywhere.
"""

def fake_llm(prompt: str) -> str:
    # Placeholder to avoid needing API keys or heavy models.
    return f"[LLM RESPONSE to prompt starting with: {prompt[:60]!r} ...]"

def summarize_paper(abstract: str) -> str:
    prompt = f"Summarize this paper abstract in 5 bullet points:\n\n{abstract}"
    return fake_llm(prompt)

def extract_insights(summary: str) -> str:
    prompt = f"From this summary, extract 3 key technical insights:\n\n{summary}"
    return fake_llm(prompt)

def generate_questions(summary: str) -> str:
    prompt = f"Given this summary, propose 3 follow-up research questions:\n\n{summary}"
    return fake_llm(prompt)

def run_pipeline(abstract: str):
    summary = summarize_paper(abstract)
    insights = extract_insights(summary)
    questions = generate_questions(summary)

    print("=== SUMMARY ===")
    print(summary)
    print("\n=== INSIGHTS ===")
    print(insights)
    print("\n=== QUESTIONS ===")
    print(questions)

if __name__ == "__main__":
    demo_abstract = (
        "We propose a new method for optimizing large language model inference "
        "by reducing KV cache memory usage while maintaining accuracy. "
        "Our approach leverages chunked attention and KV cache compression."
    )
    run_pipeline(demo_abstract)
