"""A tiny REST API. Requires: pip install fastapi uvicorn
Run:  uvicorn mini_server:app --reload
"""
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Body(BaseModel):
    msg: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/echo")
def echo(body: Body):
    return {"you_said": body.msg, "length": len(body.msg)}
