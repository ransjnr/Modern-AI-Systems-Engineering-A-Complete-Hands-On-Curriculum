# Project 13 — Agent Quality Scorecard Pipeline

Score a target system over a LangSmith dataset (LLM-as-judge correctness, embedding
similarity, a faithfulness proxy, latency) and flag regressions between versions.

## Run
```bash
pip install -r requirements.txt
cp ../../.env.example .env   # OPENAI_API_KEY + LANGCHAIN_API_KEY, LANGCHAIN_TRACING_V2=true
uvicorn app.main:app --reload --port 8010
```
```bash
curl -X POST localhost:8010/evaluate -H 'Content-Type: application/json' \
  -d '{"dataset_name":"day7-qa"}'
```
`/compare` takes two scorecards and returns a ship/block verdict.

## Tests
```bash
pytest -v -m "not live"
```
