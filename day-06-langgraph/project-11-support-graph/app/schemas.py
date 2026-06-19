from pydantic import BaseModel, Field

class TriageRequest(BaseModel):
    thread_id: str = Field(...)
    message: str = Field(..., min_length=3, max_length=2000)

class TriageDraft(BaseModel):
    thread_id: str
    category: str
    draft: str
    awaiting_approval: bool

class ApproveRequest(BaseModel):
    thread_id: str
    edited_reply: str | None = None
