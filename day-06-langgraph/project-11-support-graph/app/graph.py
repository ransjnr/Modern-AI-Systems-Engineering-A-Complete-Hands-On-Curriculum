"""Graph wiring: routing + a bounded clarify cycle + an approval interrupt."""
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from app.nodes import (SupportState, classify_node, billing_node, technical_node,
                       general_node, clarify_node)

def route_by_category(state: SupportState) -> str:
    if state["category"] == "unclear" and state.get("clarify_count", 0) < 2:
        return "clarify"
    return state["category"] if state["category"] in {"billing", "technical", "general"} \
        else "general"

def build_graph():
    g = StateGraph(SupportState)
    g.add_node("classify", classify_node)
    g.add_node("billing", billing_node)
    g.add_node("technical", technical_node)
    g.add_node("general", general_node)
    g.add_node("clarify", clarify_node)
    g.add_node("finalize", lambda s: {})
    g.add_edge(START, "classify")
    g.add_conditional_edges("classify", route_by_category, {
        "billing": "billing", "technical": "technical",
        "general": "general", "clarify": "clarify"})
    g.add_edge("clarify", "classify")           # cycle, bounded by clarify_count
    for h in ["billing", "technical", "general"]:
        g.add_edge(h, "finalize")
    g.add_edge("finalize", END)
    return g.compile(checkpointer=MemorySaver(), interrupt_before=["finalize"])

support_graph = build_graph()
