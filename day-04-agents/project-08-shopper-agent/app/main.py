from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.agent import build_agent

app = FastAPI(title="Smart Shopper Agent", version="1.0.0")
executor = build_agent(verbose=False)

class ShopRequest(BaseModel):
    query: str = Field(..., min_length=3, max_length=200)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend")
def recommend(req: ShopRequest):
    out = executor.invoke({"input":
        f"{req.query}. Compare options and return a ranked recommendation with reasons."})
    return {"recommendation": out["output"]}
