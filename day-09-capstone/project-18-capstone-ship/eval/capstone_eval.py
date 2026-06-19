"""Prove the copilot is good. Reuses the Project 17 graph and Day 7 evaluators.

Run from the Project 17 folder (so `app` imports), or set PYTHONPATH to it:
    PYTHONPATH=../project-17-copilot-core python eval/capstone_eval.py
"""
from app.graph import copilot
from langchain_openai import ChatOpenAI

judge = ChatOpenAI(model="gpt-4o-mini", temperature=0)

GOLDEN = [
    {"q": "How long do refunds take?",
     "ref": "Refunds are issued within 5 business days."},
    {"q": "What are your support hours?", "ref": "9am-6pm GMT, Monday to Friday."},
    {"q": "How do I reset my password?",
     "ref": "Use the 'Forgot password' link on the sign-in page."},
    {"q": "What's the meaning of life?",            # out-of-scope -> must not hallucinate
     "ref": "Politely says it's outside the knowledge base."},
]

def grade(question, answer, ref) -> float:
    out = judge.invoke("Grade the answer vs the reference 0-10 (reply ONLY a number).\n"
                       f"Q: {question}\nRef: {ref}\nAnswer: {answer}\nScore:").content
    digits = "".join(c for c in out if c.isdigit() or c == ".")
    try:
        return min(float(digits) / 10, 1.0)
    except ValueError:
        return 0.0

def run():
    rows, corr = [], []
    for i, ex in enumerate(GOLDEN):
        out = copilot.invoke({"message": ex["q"]},
                             {"configurable": {"thread_id": f"eval-{i}"}})
        c = grade(ex["q"], out["answer"], ex["ref"]); corr.append(c)
        rows.append({"q": ex["q"], "source": out["source"], "correctness": round(c, 2)})
    print({"avg_correctness": round(sum(corr)/len(corr), 3), "rows": rows})

if __name__ == "__main__":
    run()
