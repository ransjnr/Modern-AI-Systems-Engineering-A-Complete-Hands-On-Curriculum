from fastapi import FastAPI
from app.schemas import TriageRequest, TriageDraft, ApproveRequest
from app.graph import support_graph

app = FastAPI(title="Support Triage Graph", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "support-graph"}

@app.post("/triage", response_model=TriageDraft)
def triage(req: TriageRequest):
    cfg = {"configurable": {"thread_id": req.thread_id}}
    support_graph.invoke({"message": req.message, "clarify_count": 0}, cfg)
    state = support_graph.get_state(cfg)
    return TriageDraft(thread_id=req.thread_id,
                       category=state.values.get("category", "general"),
                       draft=state.values.get("draft", ""),
                       awaiting_approval=bool(state.next))

@app.post("/approve")
def approve(req: ApproveRequest):
    cfg = {"configurable": {"thread_id": req.thread_id}}
    if req.edited_reply:
        support_graph.update_state(cfg, {"draft": req.edited_reply})
    support_graph.invoke(None, cfg)
    final = support_graph.get_state(cfg).values
    return {"thread_id": req.thread_id, "sent_reply": final.get("draft"), "status": "sent"}
