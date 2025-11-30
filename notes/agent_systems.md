# Agent Systems Notes

- Agentic systems = LLM + tools + memory + planning.
- LangGraph models agents as nodes in a stateful graph:
  - Each node: a tool, LLM, or decision function.
  - Edges: how state flows between nodes.
- Benefits:
  - Better control over long-running workflows.
  - Easier debugging, retries, and state inspection.
- Challenges:
  - Tool call correctness and validation.
  - Handling failures and partial progress.
  - Avoiding hallucinated or unsafe tool usage.
