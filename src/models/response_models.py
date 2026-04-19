from pydantic import BaseModel

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