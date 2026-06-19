# 🚀 10-Day Tech Giants Sprint — Advanced AI/ML Engineering

> A complete, hands-on curriculum that takes you from Python foundations to shipping **production-grade AI systems** — RAG, agents, multi-agent orchestration, stateful graphs, evaluation, guardrails, deployment, and a full capstone.

This repository is the **companion codebase** to the *10-Day Tech Giants Sprint — Beginner-Friendly Manual*. Every day has its own folder; every project is a self-contained, runnable mini-application with its own README, source code, tests, and configuration.

---

## 📚 What you will build

By the end of the sprint you will have built **18 production-style projects** spanning the entire modern AI engineering stack:

| Day | Topic | Projects |
|----:|-------|----------|
| **0** | Pre-Sprint Foundations | Python · Terminal & Git · ML fundamentals · APIs · setup |
| **1** | ML / MLOps Foundations | 1 · Containerised ETA Predictor &nbsp;•&nbsp; 2 · DVC-Managed Data Pipeline |
| **2** | RAG & Vector Databases | 3 · Medical Literature RAG &nbsp;•&nbsp; 4 · Product Recommender |
| **3** | Fine-Tuning & Structured Output | 5 · QLoRA Fine-Tuner &nbsp;•&nbsp; 6 · Reliable API Layer |
| **4** | Single-Agent Design & Tools | 7 · Satellite Data Summariser &nbsp;•&nbsp; 8 · Smart Shopper Agent |
| **5** | Multi-Agent Systems | 9 · Clinical Triage Crew (CrewAI) &nbsp;•&nbsp; 10 · Software Build Team (AutoGen) |
| **6** | LangGraph — Stateful Graphs | 11 · Support Triage Graph &nbsp;•&nbsp; 12 · Self-Correcting SQL Analyst |
| **7** | Observability, Eval & Guardrails | 13 · Quality Scorecard Pipeline &nbsp;•&nbsp; 14 · Guardrails Gateway |
| **8** | Productionising & Deploying | 15 · Production Agent API &nbsp;•&nbsp; 16 · Resilient LLM Service |
| **9** | Capstone — Build & Ship | 17 · Copilot Core &nbsp;•&nbsp; 18 · Evaluate, Harden & Deploy |

---

## 🗂️ Repository structure

```
tech-giants-sprint/
├── README.md                  ← you are here
├── SETUP.md                   ← full environment setup guide
├── CURRICULUM.md              ← day-by-day learning objectives
├── RESOURCES.md               ← every doc, paper, and link, organised
├── CONTRIBUTING.md
├── LICENSE                    ← MIT
├── .env.example               ← every API key you will need
├── .gitignore
├── Makefile                   ← handy shortcuts (setup, test, lint)
├── requirements-dev.txt       ← shared dev tooling
│
├── day-00-foundations/        ← Python, terminal, Git, ML basics, setup
├── day-01-mlops/              ← Projects 1 & 2
├── day-02-rag/                ← Projects 3 & 4
├── day-03-finetuning/         ← Projects 5 & 6
├── day-04-agents/             ← Projects 7 & 8
├── day-05-multi-agent/        ← Projects 9 & 10
├── day-06-langgraph/          ← Projects 11 & 12
├── day-07-eval-guardrails/    ← Projects 13 & 14
├── day-08-production/         ← Projects 15 & 16
└── day-09-capstone/           ← Projects 17 & 18
```

Each `day-XX-*/` folder contains a `README.md` (objectives, schedule, resources) and one folder per project. Each `project-NN-*/` folder is **independently runnable** with its own README, dependencies, source, and tests.

---

## ⚡ Quick start

```bash
# 1. Clone
git clone https://github.com/ransjnr/tech-giants-sprint.git
cd tech-giants-sprint

# 2. Read the setup guide and install prerequisites
#    (Python 3.11+, Poetry, Docker, Git)  — see SETUP.md

# 3. Copy the environment template and add your keys
cp .env.example .env
#    edit .env and fill in OPENAI_API_KEY, etc.

# 4. Pick a day and a project, then follow its README
cd day-02-rag/project-03-medical-rag
poetry install
poetry run uvicorn app.main:app --reload
```

> 💡 **You do not need every API key on day one.** Each project's README lists exactly which keys it requires. Most projects run on the free tiers of OpenAI / Pinecone / Tavily / LangSmith and cost only a few cents.

---

## 🎯 Who this is for

- **Beginners** who want a guided, project-first path into modern AI engineering.
- **Engineers** who can already code but want to learn the AI/LLM production stack end to end.
- **Instructors** running a bootcamp, sprint, or university module — every day is a ready-made lesson.

No prior AI experience is required. **Day 0** brings you up to speed on Python, the terminal, Git, and ML concepts before the sprint proper begins.

---

## 🧰 The stack you will learn

`Python` · `Poetry` · `Docker` · `FastAPI` · `Pydantic v2` · `MLflow` · `DVC` ·
`OpenAI API` · `embeddings` · `Pinecone / pgvector` · `LlamaIndex` · `LoRA / QLoRA` ·
`LangChain` · `ReAct agents` · `Tavily` · `CrewAI` · `AutoGen` · `LangGraph` ·
`LangSmith` · `Ragas` · `guardrails` · `Gunicorn` · `LangServe` · `Redis` · `cloud deploy`

---

## 📖 How to use this repo with the manual

1. Read the day's chapter in the manual (the `.docx` files).
2. Open the matching `day-XX-*/README.md` here for the runnable code.
3. Build each project by following its `project-NN-*/README.md`.
4. Run the tests, then attempt the **bonus challenges** listed in each day's README.

---

## 🤝 Contributing & licence

Contributions, fixes, and new bonus challenges are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).
Licensed under the [MIT License](LICENSE). Built to be forked, taught, and improved.

> *"You started by setting up a Python environment. By Day 9 you designed, built, evaluated, hardened, and deployed a complete AI system. That is the full arc of a modern AI engineer."*
