"""State + node functions for the support graph."""
import os
from typing import TypedDict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class SupportState(TypedDict):
    message: str
    category: str
    draft: str
    clarify_count: int

def classify_node(state: SupportState) -> dict:
    out = llm.invoke(
        "Classify this support message as exactly one of: billing, technical, general, "
        "unclear (if too vague). Reply one word.\nMessage: " + state["message"]
    ).content.strip().lower()
    cat = out if out in {"billing", "technical", "general", "unclear"} else "general"
    return {"category": cat}

def _handler(area: str):
    def node(state: SupportState) -> dict:
        draft = llm.invoke(f"You are a {area} support agent. Draft a concise, friendly "
                           f"reply to:\n{state['message']}").content
        return {"draft": draft}
    return node

billing_node = _handler("billing")
technical_node = _handler("technical")
general_node = _handler("general")

def clarify_node(state: SupportState) -> dict:
    n = state.get("clarify_count", 0) + 1
    return {"draft": "Could you share a little more detail (e.g. order number or the exact "
                     "error message) so we can help?", "clarify_count": n}
