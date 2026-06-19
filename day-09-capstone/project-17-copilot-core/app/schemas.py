from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    thread_id: str = Field(...)
    message: str = Field(..., min_length=2, max_length=2000)

class ChatResponse(BaseModel):
    answer: str
    source: str
    route: str
