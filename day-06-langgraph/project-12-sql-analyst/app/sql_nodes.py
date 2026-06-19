"""Generate -> execute -> answer nodes."""
import os, json
from typing import TypedDict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from app.db import run_select, SCHEMA_DESC

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class SQLState(TypedDict):
    question: str
    sql: str
    rows: list
    error: str
    attempts: int
    answer: str

def generate_node(state: SQLState) -> dict:
    n = state.get("attempts", 0) + 1
    prompt = (f"{SCHEMA_DESC}\nWrite ONE SQLite SELECT query (no prose, no markdown) to "
              f"answer: {state['question']}")
    if state.get("error"):
        prompt += (f"\nYour previous query failed: {state['error']}\n"
                   f"Previous query: {state['sql']}\nFix it.")
    sql = llm.invoke(prompt).content.strip().strip("`").replace("sql\n", "")
    return {"sql": sql, "attempts": n}

def execute_node(state: SQLState) -> dict:
    rows, error = run_select(state["sql"])
    return {"rows": rows, "error": error}

def answer_node(state: SQLState) -> dict:
    ans = llm.invoke(f"Question: {state['question']}\nData: {json.dumps(state['rows'])}\n"
                     "Answer in one or two plain-English sentences.").content
    return {"answer": ans}
