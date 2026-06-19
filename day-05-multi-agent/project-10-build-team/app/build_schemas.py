from pydantic import BaseModel, Field
from typing import List, Dict

class BuildRequest(BaseModel):
    task: str = Field(..., min_length=10, max_length=1000)

class BuildResponse(BaseModel):
    final: str
    rounds: int
    transcript: List[Dict[str, str]]
