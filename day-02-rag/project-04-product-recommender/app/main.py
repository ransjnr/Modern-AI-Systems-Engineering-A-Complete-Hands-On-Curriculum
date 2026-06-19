from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.recommender import recommend

app = FastAPI(title="Product Recommender", version="1.0.0")

class RecRequest(BaseModel):
    interest: str = Field(..., min_length=3, max_length=300)
    k: int = Field(3, ge=1, le=10)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend")
def rec(req: RecRequest):
    try:
        return {"recommendations": recommend(req.interest, req.k)}
    except FileNotFoundError:
        raise HTTPException(503, "Index missing. Run: python app/build_index.py")
