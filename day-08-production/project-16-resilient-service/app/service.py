import time
from collections import defaultdict
from fastapi import FastAPI, Request
from pydantic import BaseModel
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.cache import lookup, store
from app.resilient import resilient_answer

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="Resilient LLM Service", version="1.0.0")
app.state.limiter = limiter

M = defaultdict(int); LAT = []

class Ask(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
@limiter.limit("30/minute")
async def ask(request: Request, body: Ask):
    t0 = time.time(); M["requests"] += 1
    cached, how = lookup(body.question)
    if cached is not None:
        M["cache_" + how] += 1; LAT.append(time.time() - t0)
        return {"answer": cached, "cache": how}
    M["cache_miss"] += 1
    out = await resilient_answer(body.question)
    store(body.question, out["answer"])
    M["source_" + out["source"]] += 1; LAT.append(time.time() - t0)
    return {"answer": out["answer"], "cache": "miss", "source": out["source"]}

@app.get("/metrics")
def metrics():
    total = M["requests"] or 1
    hits = M["cache_exact"] + M["cache_semantic"]
    p95 = round(sorted(LAT)[int(len(LAT) * 0.95)], 3) if LAT else 0.0
    return {"requests": M["requests"], "cache_hit_rate": round(hits/total, 3),
            "fallback_rate": round((M["source_fallback-mini"] +
                                    M["source_fallback-canned"]) / total, 3),
            "p95_latency_s": p95, "raw": dict(M)}
