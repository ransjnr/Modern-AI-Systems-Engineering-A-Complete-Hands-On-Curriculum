from pydantic import BaseModel, Field

class ReportRequest(BaseModel):
    satellite: str = Field(..., min_length=2, max_length=80)

class ReportResponse(BaseModel):
    report: str
