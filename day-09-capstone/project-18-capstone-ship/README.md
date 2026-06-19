# Project 18 — Capstone Ship: Evaluate, Harden & Deploy

Turn the Copilot Core (Project 17) into a shipped product: run a scorecard, wrap it in the
Day-8 production shell, deploy to a live URL, and prepare the 5-minute pitch.

## Steps
1. **Evaluate** — run `eval/capstone_eval.py` over a small labelled set (correctness +
   faithfulness, including an out-of-scope case it must refuse).
2. **Harden** — reuse Day 8: `app/config.py`, the multi-stage `Dockerfile`, docker-compose
   with Redis, exact+semantic cache, `/health` + `/ready`. The Copilot graph is the app.
3. **Deploy** — follow `DEPLOY.md` (Render / Railway / Fly.io / HF Spaces) for a live URL.
4. **Pitch** — fill in `PITCH.md` and make one architecture slide.

## Run the scorecard
```bash
pip install langchain-openai openai numpy
# point PYTHONPATH at Project 17 so the graph is importable, then:
python eval/capstone_eval.py
```

## What "done" looks like
- Scorecard prints average correctness + faithfulness; the out-of-scope case does not hallucinate.
- Service runs in Docker with `/health` + caching; a live URL exists.
- `PITCH.md` + one architecture slide are ready, including a rehearsed failure-path moment.
