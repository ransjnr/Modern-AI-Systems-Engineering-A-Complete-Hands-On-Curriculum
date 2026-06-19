"""Run a target over the dataset and aggregate the scores."""
import time
from langsmith import Client
from langchain_openai import ChatOpenAI
from app.evaluators import similarity, judge_correctness

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def target(question: str) -> str:
    return llm.invoke(f"Answer briefly and accurately: {question}").content

def run_scorecard(dataset_name: str) -> dict:
    examples = list(Client().list_examples(dataset_name=dataset_name))
    rows, sims, judges, lat = [], [], [], []
    for ex in examples:
        q, ref = ex.inputs["question"], ex.outputs["answer"]
        t0 = time.time(); ans = target(q); dt = round(time.time() - t0, 3)
        s = round(similarity(ans, ref), 3); j = round(judge_correctness(q, ans, ref), 3)
        sims.append(s); judges.append(j); lat.append(dt)
        rows.append({"question": q, "answer": ans, "similarity": s, "judge": j,
                     "latency_s": dt})
    n = len(rows) or 1
    return {"n": len(rows), "avg_similarity": round(sum(sims)/n, 3),
            "avg_judge": round(sum(judges)/n, 3), "avg_latency_s": round(sum(lat)/n, 3),
            "rows": rows}
