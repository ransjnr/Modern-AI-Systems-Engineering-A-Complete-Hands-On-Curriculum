# Project 15 — Production Agent API

A hardened, deployable FastAPI service: env-based config, request-ID JSON logging,
liveness/readiness probes, an async endpoint, a LangServe route, multi-stage Docker,
and docker-compose with Redis.

## Run locally
```bash
pip install -r requirements.txt
cp ../../.env.example .env     # OPENAI_API_KEY required
uvicorn app.main:app --reload --port 8012
```

## Run in Docker (production shape)
```bash
docker compose up --build      # Gunicorn + Uvicorn workers + Redis
curl localhost:8012/health
curl localhost:8012/ready
```

## Deploy
See `DEPLOY.md` for Render / Railway / Fly.io / HF Spaces.

## Endpoints
`GET /health` · `GET /ready` · `POST /ask` · LangServe `/chat/{invoke,stream,playground}`

## Tests
```bash
pytest -v
```
