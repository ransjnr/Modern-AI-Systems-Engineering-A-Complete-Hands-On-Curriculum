import os
from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from app.schemas import ChatRequest, ChatResponse
from app.guards_in import check_input
from app.guards_out import check_output, SAFE_REFUSAL

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
app = FastAPI(title="Guardrails Gateway", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "guardrails-gateway"}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    gin = check_input(req.message)                      # INPUT GUARDRAILS
    if not gin.allowed:
        return ChatResponse(allowed=False, answer=SAFE_REFUSAL, block_reason=gin.reason)
    raw = llm.invoke("You are a helpful, safe assistant. Answer concisely.\n"
                     f"User: {gin.cleaned}").content    # model sees only cleaned text
    gout = check_output(raw)                            # OUTPUT GUARDRAILS
    if not gout.allowed:
        return ChatResponse(allowed=False, answer=SAFE_REFUSAL,
                            pii_redacted=gin.pii_found, block_reason=gout.reason)
    return ChatResponse(allowed=True, answer=gout.text, pii_redacted=gin.pii_found)
