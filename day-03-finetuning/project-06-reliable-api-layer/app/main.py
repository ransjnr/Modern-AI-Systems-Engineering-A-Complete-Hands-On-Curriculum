from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.schemas import SupportTicket
from app.extract import extract_ticket

app = FastAPI(title="Reliable Structured-Output API", version="1.0.0")

class ExtractRequest(BaseModel):
    text: str = Field(..., min_length=5, max_length=2000)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/extract", response_model=SupportTicket)
def extract(req: ExtractRequest):
    try:
        return extract_ticket(req.text)
    except Exception as e:
        raise HTTPException(422, f"Could not extract a valid ticket: {e}")
