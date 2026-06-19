from pydantic import BaseModel, Field

class TriageRequest(BaseModel):
    complaint: str = Field(..., min_length=5, max_length=2000)

class TriageResponse(BaseModel):
    briefing: str
    disclaimer: str = ("Informational support only. Not a medical diagnosis. "
                       "Consult a qualified clinician.")
