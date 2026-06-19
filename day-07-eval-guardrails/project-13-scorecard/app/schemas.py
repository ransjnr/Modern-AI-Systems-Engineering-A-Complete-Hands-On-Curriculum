from pydantic import BaseModel
from typing import List, Dict, Any

class EvalRequest(BaseModel):
    dataset_name: str = "day7-qa"

class Scorecard(BaseModel):
    n: int
    avg_similarity: float
    avg_judge: float
    avg_latency_s: float
    rows: List[Dict[str, Any]]

class CompareRequest(BaseModel):
    baseline: Scorecard
    candidate: Scorecard
