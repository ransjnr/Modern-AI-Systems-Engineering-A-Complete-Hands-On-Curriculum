# Project 9 — Clinical Triage & Research Crew (CrewAI)

Four specialised agents collaborate to turn a free-text complaint into a cautious,
structured triage briefing. Intake → Researcher (tool) → Differential → Safety/Writer.

> ⚠️ Information support only — NOT a diagnosis. Safety is built into every agent's prompt.

## Run
```bash
pip install -r requirements.txt
cp ../../.env.example .env       # OPENAI_API_KEY required
uvicorn app.main:app --reload --port 8006
```
```bash
curl -X POST localhost:8006/triage -H 'Content-Type: application/json' \
  -d '{"complaint":"Dull headache for two days, worse in the evenings, no fever."}'
```

## Tests
```bash
pytest -v -m "not live"   # fast; add nothing to include the live crew run
```
