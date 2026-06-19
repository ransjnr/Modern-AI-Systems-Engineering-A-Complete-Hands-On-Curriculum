# Day 7 — Observability, Evaluation & Guardrails

Stop building, start measuring. Trace what your system does, score whether it's good, and
guard against the ways it goes wrong.

## Projects
| # | Project | Folder | Stack |
|---|---------|--------|-------|
| 13 | Agent Quality Scorecard Pipeline | `project-13-scorecard/` | LangSmith · Ragas-style evaluators |
| 14 | Guardrails Gateway | `project-14-guardrails-gateway/` | PII/injection in · schema/safety out |

## Keys
`OPENAI_API_KEY` (both). `LANGCHAIN_API_KEY` + `LANGCHAIN_TRACING_V2=true` (Project 13 tracing).

## Learning objectives
- Enable LangSmith tracing and read a trace to debug.
- Build a dataset + evaluators (similarity, LLM-as-judge, faithfulness) and a regression gate.
- Implement input guardrails (PII redaction, injection detection) and output guardrails (schema/safety), returning a safe refusal on failure.

> 🛡️ The gateway is **defensive only** — it detects and blocks, never produces unsafe content. Treat guardrails as layered defence in depth.

## Bonus
- Wire `/compare` into a CI gate that fails the build on regression.
- Build a 10-case adversarial set and measure the gateway's catch rate.

## Resources
See **Day 7** in [../RESOURCES.md](../RESOURCES.md).
