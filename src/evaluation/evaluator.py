from models.evaluation_models import EvaluationMetrics

from evaluation.metrics import (
    score_structure,
    score_relevance,
    score_detail,
    score_consistency,
    score_latency
)


def evaluate_output(output: dict) -> EvaluationMetrics:
    return EvaluationMetrics(
        structure_score=score_structure(output),
        relevance_score=score_relevance(output),
        detail_score=score_detail(output),
        consistency_score=score_consistency(output),
        latency_score=score_latency(output)
    )