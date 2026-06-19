# Day 4 — Single-Agent Design & Intelligent Tool Use

The LLM becomes the decision-maker. Learn the ReAct loop, build LangChain agents, create
custom tools, and give an agent live web search.

## Projects
| # | Project | Folder | Stack |
|---|---------|--------|-------|
| 7 | Satellite Data Summariser | `project-07-satellite-agent/` | LangChain · ReAct · custom tools |
| 8 | Smart Shopper Agent | `project-08-shopper-agent/` | LangChain · Tavily search |

## Keys
`OPENAI_API_KEY` (both). `TAVILY_API_KEY` (Project 8, and optional in Project 7).

## Learning objectives
- Explain the ReAct loop (Thought → Action → Observation → … → Final Answer).
- Build an `AgentExecutor` with multiple tools; write high-quality tool descriptions.
- Integrate Tavily for real-time web search; read intermediate steps to debug.

## Bonus
- Swap `create_react_agent` for `create_openai_tools_agent` and compare step counts.
- Add `ConversationBufferWindowMemory` so the agent remembers prior turns.

## Resources
See **Day 4** in [../RESOURCES.md](../RESOURCES.md).
