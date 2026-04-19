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

def score_latency(output: dict) -> float:
    latency_ms = output.get("latency_ms", 0)
    if latency_ms < 2000:
        return 100
    elif latency_ms < 5000:
        return 80
    elif latency_ms < 10000:
        return 60
    else:
        return 30