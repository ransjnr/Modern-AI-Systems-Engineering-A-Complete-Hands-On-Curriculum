"""The self-correction cycle: generate -> execute -> (retry | answer)."""
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from app.sql_nodes import SQLState, generate_node, execute_node, answer_node

MAX_TRIES = 3

def after_execute(state: SQLState) -> str:
    if not state["error"] and state["rows"] is not None:
        return "answer"
    if state["attempts"] < MAX_TRIES:
        return "retry"
    return "answer"

def build_sql_graph():
    g = StateGraph(SQLState)
    g.add_node("generate", generate_node)
    g.add_node("execute", execute_node)
    g.add_node("answer", answer_node)
    g.add_edge(START, "generate")
    g.add_edge("generate", "execute")
    g.add_conditional_edges("execute", after_execute,
                            {"retry": "generate", "answer": "answer"})
    g.add_edge("answer", END)
    return g.compile(checkpointer=MemorySaver())

sql_graph = build_sql_graph()
