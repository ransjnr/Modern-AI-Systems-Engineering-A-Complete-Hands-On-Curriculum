# Project 7 — SpaceTech Satellite Data Summariser

A LangChain ReAct agent with multiple tools (a mock satellite DB, orbital-mechanics
calculator, optional web search, and a report formatter). The agent decides which tools
to call, in what order, to build an intelligence report.

## Run
```bash
pip install -r requirements.txt
cp ../../.env.example .env     # OPENAI_API_KEY required; TAVILY optional
uvicorn app.main:app --reload  # :8004
```
```bash
curl -X POST localhost:8004/satellite-report -H 'Content-Type: application/json' \
  -d '{"satellite":"ISS"}'
```
Run with verbose ReAct trace:
```bash
python app/agent.py
```
