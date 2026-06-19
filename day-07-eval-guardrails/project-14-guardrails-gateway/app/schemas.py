from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)

class ChatResponse(BaseModel):
    allowed: bool
    answer: str
    pii_redacted: list[str] = []
    block_reason: str = ""
