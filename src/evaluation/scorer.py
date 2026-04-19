from models.evaluation_models import EvaluationMetrics


WEIGHTS = {
    "structure": 0.25,
    "relevance": 0.35,
    "detail": 0.2,
    "consistency": 0.2
}


def compute_final_score(metrics: EvaluationMetrics) -> float:
    return (
        metrics.structure_score * WEIGHTS["structure"] +
        metrics.relevance_score * WEIGHTS["relevance"] +
        metrics.detail_score * WEIGHTS["detail"] +
        metrics.consistency_score * WEIGHTS["consistency"]
    )