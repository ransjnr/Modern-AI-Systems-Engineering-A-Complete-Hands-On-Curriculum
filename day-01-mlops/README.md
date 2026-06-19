# Day 1 — ML / MLOps Foundations

Everything you learn today is used every remaining day: Poetry, Pydantic v2, Docker, MLflow, DVC.

## Projects
| # | Project | Folder | Stack |
|---|---------|--------|-------|
| 1 | Containerised ETA Predictor | `project-01-eta-predictor/` | FastAPI · scikit-learn · Docker · MLflow |
| 2 | DVC-Managed Data Pipeline | `project-02-dvc-pipeline/` | DVC · scikit-learn |

## Learning objectives
- Manage dependencies with Poetry; validate I/O with Pydantic v2.
- Write a production multi-stage Dockerfile and orchestrate with docker-compose.
- Track experiments with MLflow; version data & pipelines with DVC.

## Bonus challenges
- Add a `/batch` endpoint that predicts for a list of inputs.
- Log feature importances to MLflow and compare two runs in the UI.
- Add a 4th DVC stage that produces a calibration plot artifact.

## Resources
See **Day 1 — MLOps** in [../RESOURCES.md](../RESOURCES.md).
