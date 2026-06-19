from fastapi import FastAPI
from app.schemas import ReportRequest, ReportResponse
from app.agent import build_agent

app = FastAPI(title="Satellite Data Summariser", version="1.0.0")
executor = build_agent(verbose=False)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/satellite-report", response_model=ReportResponse)
def report(req: ReportRequest):
    out = executor.invoke({"input":
        f"Build an intelligence report on {req.satellite}, including its orbit."})
    return ReportResponse(report=out["output"])
