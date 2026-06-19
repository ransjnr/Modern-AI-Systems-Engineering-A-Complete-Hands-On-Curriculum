# 📘 Curriculum — Day-by-Day Learning Objectives

Each day runs 09:00–21:00 (training → building → demo) and ships two production-style projects. Projects are numbered **sequentially** across the whole sprint (Day _N_ → Projects _2N-1_ and _2N_).

---

## Day 0 — Pre-Sprint Foundations *(self-paced, before Day 1)*
Python for ML · the terminal · Git & GitHub · ML fundamentals · software engineering · APIs & HTTP · AI/LLM concepts · environment setup.
**Outcome:** you can write Python functions/classes, use the terminal and Git, explain supervised vs unsupervised learning, and have all tools installed.

## Day 1 — ML / MLOps Foundations
Poetry · Pydantic v2 · Docker · MLflow · DVC.
**Projects:** 1) Containerised ETA Predictor (FastAPI + Docker + MLflow) · 2) DVC-Managed Data Pipeline.

## Day 2 — RAG & Vector Databases
LLM basics · embeddings · vector DBs · chunking · RAG pipeline · hybrid search · re-ranking.
**Projects:** 3) Medical Literature RAG · 4) Product Recommender with vector similarity.

## Day 3 — Fine-Tuning & Structured Output
Fine-tune vs RAG vs prompt-engineering · LoRA / QLoRA · prompt engineering · JSON mode & function calling.
**Projects:** 5) QLoRA Fine-Tuner · 6) Reliable structured-output API layer.

## Day 4 — Single-Agent Design & Intelligent Tool Use
What an agent is · the ReAct loop · LangChain agents · custom tools · Tavily search · agent memory.
**Projects:** 7) Satellite Data Summariser · 8) Smart Shopper Agent.

## Day 5 — Multi-Agent Systems
Orchestration patterns (sequential / hierarchical / group chat) · CrewAI · AutoGen · code execution · termination & cost control.
**Projects:** 9) Clinical Triage Crew (CrewAI) · 10) Software Build Team (AutoGen).

## Day 6 — LangGraph: Stateful Agent Graphs
State · nodes · edges · conditional routing · cycles & the reflection pattern · checkpointing & memory · human-in-the-loop.
**Projects:** 11) Support Triage Graph · 12) Self-Correcting SQL Analyst.

## Day 7 — Observability, Evaluation & Guardrails
LangSmith tracing · datasets & evaluators · LLM-as-judge · Ragas (faithfulness) · input/output guardrails · regression testing.
**Projects:** 13) Quality Scorecard Pipeline · 14) Guardrails Gateway.

## Day 8 — Productionising & Deploying Agents
Production Docker · Gunicorn + Uvicorn workers · LangServe · caching (exact + semantic) · rate limiting · retries/timeouts/fallback · health & readiness · load testing · cloud deploy.
**Projects:** 15) Production Agent API · 16) Resilient LLM Service.

## Day 9 — Capstone: Build & Ship an End-to-End System
System design · integration patterns · composing RAG + graph + guardrails + eval + deploy · presenting & defending.
**Projects:** 17) Copilot Core (integration) · 18) Evaluate, Harden & Deploy.

---

### The throughline
Every day builds on the last: foundations → reproducible ML → retrieval → specialisation → one agent → many agents → explicit graphs → measuring & guarding → shipping → composing it all into one deployable product.
