from fastapi import FastAPI, HTTPException
from app.schemas import EvalRequest, Scorecard, CompareRequest
from app.dataset import ensure_dataset
from app.scorecard import run_scorecard

app = FastAPI(title="Agent Quality Scorecard", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "scorecard"}

@app.post("/evaluate", response_model=Scorecard)
def evaluate_endpoint(req: EvalRequest):
    try:
        return Scorecard(**run_scorecard(ensure_dataset(req.dataset_name)))
    except Exception as e:
        raise HTTPException(500, str(e))

@app.post("/compare")
def compare(req: CompareRequest):
    d = {"similarity": round(req.candidate.avg_similarity - req.baseline.avg_similarity, 3),
         "judge": round(req.candidate.avg_judge - req.baseline.avg_judge, 3),
         "latency_s": round(req.candidate.avg_latency_s - req.baseline.avg_latency_s, 3)}
    regression = d["similarity"] < -0.02 or d["judge"] < -0.02
    return {"deltas": d, "regression": regression,
            "verdict": "BLOCK - quality regressed" if regression else "OK to ship"}
