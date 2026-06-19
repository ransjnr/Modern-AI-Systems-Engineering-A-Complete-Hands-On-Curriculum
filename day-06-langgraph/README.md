# Day 6 — LangGraph: Stateful Agent Graphs

Draw your workflow as an explicit graph: state, nodes, edges, conditional routing,
cycles, checkpointing/memory, and human-in-the-loop.

## Projects
| # | Project | Folder | Stack |
|---|---------|--------|-------|
| 11 | Support Triage & Resolution Graph | `project-11-support-graph/` | LangGraph (routing + cycle + interrupt) |
| 12 | Self-Correcting SQL Analyst | `project-12-sql-analyst/` | LangGraph (reflection cycle) + SQLite |

## Keys
`OPENAI_API_KEY` (both).

## Learning objectives
- Build a `StateGraph`: typed state, nodes, edges, entry point, compile, invoke.
- Add conditional edges (routing) and safe cycles (reflection), bounded by a counter + `recursion_limit`.
- Add a checkpointer + `thread_id` for memory; pause for approval with `interrupt_before`.

## Bonus
- Stream node outputs with `app.stream(...)`.
- Swap `MemorySaver` for the SQLite checkpointer (durable memory).

## Resources
See **Day 6** in [../RESOURCES.md](../RESOURCES.md).
