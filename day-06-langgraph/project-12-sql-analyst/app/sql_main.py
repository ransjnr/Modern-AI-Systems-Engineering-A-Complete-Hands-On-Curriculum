from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.sql_graph import sql_graph

app = FastAPI(title="Self-Correcting SQL Analyst", version="1.0.0")

class AskRequest(BaseModel):
    thread_id: str = Field(...)
    question: str = Field(..., min_length=5, max_length=500)

class AskResponse(BaseModel):
    sql: str
    answer: str
    attempts: int

@app.get("/health")
def health():
    return {"status": "ok", "service": "sql-analyst"}

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    cfg = {"configurable": {"thread_id": req.thread_id}}
    try:
        out = sql_graph.invoke(
            {"question": req.question, "attempts": 0, "error": "", "rows": None},
            cfg | {"recursion_limit": 15})
    except Exception as e:
        raise HTTPException(500, str(e))
    return AskResponse(sql=out["sql"], answer=out["answer"], attempts=out["attempts"])
