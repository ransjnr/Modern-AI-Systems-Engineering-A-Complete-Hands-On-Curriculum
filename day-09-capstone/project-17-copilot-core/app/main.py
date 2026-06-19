from fastapi import FastAPI, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.graph import copilot

app = FastAPI(title="Enterprise Copilot (Capstone)", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "capstone-copilot"}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    cfg = {"configurable": {"thread_id": req.thread_id}}
    try:
        out = copilot.invoke({"message": req.message}, cfg | {"recursion_limit": 12})
    except Exception as e:
        raise HTTPException(500, str(e))
    return ChatResponse(answer=out["answer"], source=out["source"], route=out["route"])
