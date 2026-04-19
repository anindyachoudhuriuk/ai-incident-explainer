from pydantic import BaseModel, Field

class EvaluationMetrics(BaseModel):
    model: str
    structure_score: float = Field(ge=0, le=100)
    relevance_score: float = Field(ge=0, le=100)
    detail_score: float = Field(ge=0, le=100)
    consistency_score: float = Field(ge=0, le=100)
    latency_score: float = Field(ge=0, le=100)

class EvaluationResult(BaseModel):
    metrics: EvaluationMetrics
    final_score: float = Field(ge=0, le=100)
    model_name: str
    incident_id: str