from pydantic import BaseModel, Field

class RootCause(BaseModel):
    cause: str
    description: str

class Analysis(BaseModel):
    what_happened: str
    root_causes: list[RootCause]

class Incident(BaseModel):
    system: str
    error: str
    context: str

class ResponseSchema(BaseModel):
    incident: Incident
    analysis: Analysis
    latency_ms: float
    model: str
    
class JudgeSchema(BaseModel):
    incident: Incident
    relevance: int = Field(ge=0, le=3)
    completeness: int = Field(ge=0, le=3)
    clarity: int = Field(ge=0, le=3)
    latency_ms: float
    model: str