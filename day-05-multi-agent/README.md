# Day 5 — Multi-Agent Systems (CrewAI & AutoGen)

Several specialised agents collaborate. Learn the three orchestration patterns
(sequential, hierarchical, group chat), CrewAI, and AutoGen with code execution.

## Projects
| # | Project | Folder | Stack |
|---|---------|--------|-------|
| 9 | Clinical Triage & Research Crew | `project-09-triage-crew/` | CrewAI (sequential) |
| 10 | Multi-Agent Software Build Team | `project-10-build-team/` | AutoGen (group chat) |

## Keys
`OPENAI_API_KEY` (both).

## Learning objectives
- Choose sequential vs hierarchical vs group-chat orchestration.
- Build a CrewAI crew (Agent/Task/Crew/Process) with tools and context handoffs.
- Build an AutoGen group chat with code execution and reliable termination.
- Control cost and prevent infinite loops (`max_round`, `max_iterations`, TERMINATE).

> ⚠️ Project 9 is an information-support tool, **not** medical diagnosis — safety is built into every prompt. Project 10's Executor runs model-written code; use a sandbox (`use_docker=True` in production).

## Bonus
- Convert Project 9 to `Process.hierarchical` and compare extra LLM calls.
- Switch Project 10 to `speaker_selection_method="auto"` and observe behaviour.

## Resources
See **Day 5** in [../RESOURCES.md](../RESOURCES.md).
