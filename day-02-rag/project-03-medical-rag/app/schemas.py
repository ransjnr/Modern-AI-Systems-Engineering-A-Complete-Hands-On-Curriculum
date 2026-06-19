from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    question: str = Field(..., min_length=5, max_length=500)

class AskResponse(BaseModel):
    answer: str
    sources: list[str]
    disclaimer: str = "Educational only. Not medical advice. Consult a clinician."
