from fastapi import FastAPI, HTTPException
from app.schemas import AskRequest, AskResponse
from app.rag import answer

app = FastAPI(title="Medical Literature RAG", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    try:
        out = answer(req.question)
    except FileNotFoundError:
        raise HTTPException(503, "Index missing. Run: python app/ingest.py")
    return AskResponse(**out)
