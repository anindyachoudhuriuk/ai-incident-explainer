from pydantic import BaseModel, Field

class ModelConfig(BaseModel):
    model: str
    temperature: float = Field(ge=0, le=1)
    max_tokens: int = Field(gt=0)