# Project 2 — DVC-Managed Data Pipeline

Version data and define a reproducible 3-stage pipeline (prepare → featurize → evaluate) so any engineer can reproduce your exact results.

## Setup
```bash
pip install dvc scikit-learn pandas numpy joblib pyyaml
git init && dvc init
```

## Run the pipeline
```bash
dvc repro            # runs all stages defined in dvc.yaml
dvc metrics show     # shows metrics/scores.json
dvc dag              # visualise the pipeline graph
```

Change a value in `params.yaml`, then `dvc repro` again — DVC only re-runs the affected stages.

## Stages (dvc.yaml)
1. **prepare** — generate/clean the dataset → `data/prepared.csv`
2. **featurize** — engineer features → `data/features.csv`
3. **evaluate** — train + score, write `metrics/scores.json`

## Remote storage (optional)
```bash
dvc remote add -d storage s3://your-bucket/dvcstore   # or gdrive/local
dvc push
```
