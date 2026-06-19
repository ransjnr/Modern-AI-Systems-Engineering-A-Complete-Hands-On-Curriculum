import logging, json, time, uuid
import redis
from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import AsyncOpenAI
from app.config import settings

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("app")
def jlog(**kv): log.info(json.dumps(kv))

app = FastAPI(title="Production Agent API", version="1.0.0")
client = AsyncOpenAI(api_key=settings.openai_api_key, timeout=settings.request_timeout_s)
r = redis.from_url(settings.redis_url)

class Ask(BaseModel):
    question: str

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    rid = str(uuid.uuid4())[:8]; t0 = time.time()
    response = await call_next(request)
    jlog(event="request", id=rid, path=request.url.path,
         status=response.status_code, ms=round((time.time()-t0)*1000))
    response.headers["X-Request-ID"] = rid
    return response

@app.get("/health")           # LIVENESS
def health():
    return {"status": "ok"}

@app.get("/ready")            # READINESS
def ready():
    checks = {"redis": False, "openai_key": bool(settings.openai_api_key)}
    try:
        r.ping(); checks["redis"] = True
    except Exception:
        pass
    return {"ready": all(checks.values()), "checks": checks}

@app.post("/ask")
async def ask(req: Ask):
    resp = await client.chat.completions.create(
        model=settings.model, messages=[{"role": "user", "content": req.question}])
    return {"answer": resp.choices[0].message.content}
