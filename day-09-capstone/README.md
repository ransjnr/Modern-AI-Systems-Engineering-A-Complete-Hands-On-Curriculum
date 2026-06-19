# Day 9 — Capstone: Build & Ship an End-to-End AI System

Compose the whole week into one system: RAG + an orchestrator graph + guardrails + an
evaluation scorecard + production deployment. The worked example is an **Enterprise
Support & Knowledge Copilot**.

## Projects
| # | Project | Folder | What it adds |
|---|---------|--------|--------------|
| 17 | Copilot Core | `project-17-copilot-core/` | the integration: guard → route → retrieve/tool/escalate → guard |
| 18 | Capstone Ship | `project-18-capstone-ship/` | evaluate (scorecard), harden (Day 8 shell), deploy, pitch |

## Keys
`OPENAI_API_KEY` (required). LangSmith optional for tracing.

## The reference architecture
```
user -> [production shell: cache/rate-limit/retry/health]
     -> INPUT GUARDRAILS (PII, injection)
     -> ORCHESTRATOR GRAPH (classify & route)
          -> retrieve from KB (RAG)  |  call a tool  |  escalate to human
     -> generate grounded answer
     -> OUTPUT GUARDRAILS (faithfulness, safety)
     -> answer        (traced end-to-end; evaluated offline by the scorecard)
```

## Apply it to YOUR problem
The example is a copilot; the architecture is general. Pick a problem, choose which boxes
you need (see the decision guide in the manual), and swap the tiny KB + stub tool for real
ones.

## Bonus
- Add a feedback endpoint that writes failed questions into the eval set.
- Swap the in-memory KB for a real vector store (Day 2) and re-run the scorecard.

## Resources
See **Day 9** in [../RESOURCES.md](../RESOURCES.md).
