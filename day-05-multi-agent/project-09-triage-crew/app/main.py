from fastapi import FastAPI, HTTPException
from app.schemas import TriageRequest, TriageResponse
from app.crew import run_triage

app = FastAPI(title="Clinical Triage Crew", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "triage-crew"}

@app.post("/triage", response_model=TriageResponse)
def triage(req: TriageRequest):
    try:
        return TriageResponse(briefing=run_triage(req.complaint))
    except Exception as e:
        raise HTTPException(500, f"Crew failed: {e}")
