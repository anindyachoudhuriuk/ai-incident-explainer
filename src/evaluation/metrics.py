def score_structure(output: dict) -> float:
    required_fields = ["id", "summary", "what_happened", "root_cause"]
    present = sum(1 for f in required_fields if f in output and output[f])

    return (present / len(required_fields)) * 100


def score_relevance(output: dict) -> float:
    # simple heuristic (can upgrade to LLM judge later)
    explanation = output.get("what_happened", "")
    return min(len(explanation) / 5, 100)


def score_detail(output: dict) -> float:
    return min(len(output.get("root_cause", "")) / 5, 100)


def score_consistency(output: dict) -> float:
    # placeholder (can expand with multi-run comparison)
    return 80.0