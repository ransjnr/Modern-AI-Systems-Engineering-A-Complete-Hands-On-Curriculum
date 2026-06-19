# Day 8 — Productionising & Deploying Agents

Close the gap between "runs on my laptop" and "serves real users reliably, for cents."

## Projects
| # | Project | Folder | Stack |
|---|---------|--------|-------|
| 15 | Production Agent API | `project-15-production-api/` | Docker · Gunicorn · LangServe · Redis |
| 16 | Resilient LLM Service | `project-16-resilient-service/` | cache · retry/fallback · rate limit · load test |

## Keys
`OPENAI_API_KEY` (both). `REDIS_URL` (compose provides Redis).

## Learning objectives
- Write a hardened multi-stage Dockerfile (slim, non-root, HEALTHCHECK).
- Serve with Gunicorn + Uvicorn workers; expose chains via LangServe.
- Add caching (exact + semantic), rate limiting, retries/timeouts/fallback.
- Distinguish liveness vs readiness; load-test; deploy to a free cloud target.

## Bonus
- Add CI/CD that builds the image and runs smoke tests.
- Swap the in-memory semantic cache for a Redis-backed shared cache.

## Resources
See **Day 8** in [../RESOURCES.md](../RESOURCES.md).
