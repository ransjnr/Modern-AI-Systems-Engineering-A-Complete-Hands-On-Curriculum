# Project 10 — Multi-Agent Software Build Team (AutoGen)

An AutoGen group chat that writes and tests software on request: Planner → Coder →
Executor (runs the code) → Reviewer, iterating until the tests pass.

> ⚠️ The Executor runs model-written code. In the sandbox/Codespaces `use_docker=False`
> is fine; in production use `use_docker=True` and never point `work_dir` at important files.

## Run
```bash
pip install -r requirements.txt
cp ../../.env.example .env       # OPENAI_API_KEY required
uvicorn app.build_main:app --reload --port 8007
```
```bash
curl -X POST localhost:8007/build -H 'Content-Type: application/json' \
  -d '{"task":"Write first_n_primes(n) returning the first n primes, with asserts."}'
```

## Tests
```bash
pytest -v -m "not live"
```
