"""The orchestrator graph - this is where the week comes together."""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from app.kb import retrieve
from app.guards import guard_input, guard_output

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class CoState(TypedDict):
    message: str
    cleaned: str
    route: str
    contexts: list
    answer: str
    source: str
    blocked_reason: str

def input_guard(state: CoState) -> dict:
    ok, cleaned, reason = guard_input(state["message"])
    return {"cleaned": cleaned, "route": "blocked" if not ok else "",
            "blocked_reason": reason}

def classify(state: CoState) -> dict:
    if state["route"] == "blocked":
        return {}
    d = llm.invoke(
        "Classify the request as one word: 'tool' if it asks to look up an order/account "
        "by id, 'escalate' if a complaint/sensitive, else 'answer'.\n"
        f"Request: {state['cleaned']}").content.strip().lower()
    return {"route": d if d in {"tool", "escalate", "answer"} else "answer"}

def retrieve_answer(state: CoState) -> dict:
    ctx = retrieve(state["cleaned"])
    if not ctx:
        return {"answer": "I don't have that in my knowledge base. Let me hand you to a "
                          "human who can help.", "source": "no-match", "contexts": []}
    grounded = llm.invoke(
        "Answer ONLY from the context; if it's not there, say you don't know.\n"
        f"Context:\n{chr(10).join(ctx)}\n\nQuestion: {state['cleaned']}").content
    return {"answer": grounded, "source": "knowledge-base", "contexts": ctx}

def use_tool(state: CoState) -> dict:
    return {"answer": "Order #12345 shipped on 6 May and arrives 9 May.",
            "source": "order-tool", "contexts": []}

def escalate(state: CoState) -> dict:
    return {"answer": "This needs a specialist - I've created a ticket and a human will "
                      "follow up shortly.", "source": "human-escalation", "contexts": []}

def blocked(state: CoState) -> dict:
    return {"answer": "I can't process that request.", "source": "guardrail",
            "contexts": []}

def output_guard(state: CoState) -> dict:
    ok, _ = guard_output(state["answer"], state.get("contexts", []))
    if not ok:
        return {"answer": "I can't share that response.", "source": "guardrail-out"}
    return {}

def route_decider(state: CoState) -> str:
    return state["route"] or "answer"

def build_copilot():
    g = StateGraph(CoState)
    for name, fn in [("input_guard", input_guard), ("classify", classify),
                     ("answer", retrieve_answer), ("tool", use_tool),
                     ("escalate", escalate), ("blocked", blocked),
                     ("output_guard", output_guard)]:
        g.add_node(name, fn)
    g.add_edge(START, "input_guard")
    g.add_edge("input_guard", "classify")
    g.add_conditional_edges("classify", route_decider,
        {"answer": "answer", "tool": "tool", "escalate": "escalate", "blocked": "blocked"})
    for n in ["answer", "tool", "escalate", "blocked"]:
        g.add_edge(n, "output_guard")
    g.add_edge("output_guard", END)
    return g.compile(checkpointer=MemorySaver())

copilot = build_copilot()
