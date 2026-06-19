# Day 3 — Fine-Tuning & Structured Output

When to fine-tune vs RAG vs prompt-engineering; LoRA/QLoRA; and getting reliable, structured JSON out of an LLM.

## Projects
| # | Project | Folder | Stack |
|---|---------|--------|-------|
| 5 | QLoRA Fine-Tuner | `project-05-qlora-finetuner/` | transformers · PEFT · bitsandbytes |
| 6 | Reliable API Layer | `project-06-reliable-api-layer/` | OpenAI function calling · Pydantic · retry |

## ⚠️ GPU note (Project 5)
QLoRA needs a CUDA GPU (a free Google Colab T4 is enough). On CPU-only machines, read the code and run Project 6 instead, or use the provided Colab cell. Project 6 needs only an `OPENAI_API_KEY`.

## Learning objectives
- Choose between fine-tuning, RAG, and prompt-engineering.
- Understand LoRA (low-rank adapters) and QLoRA (4-bit + LoRA).
- Force reliable structured output via JSON mode and function calling, with retry/repair.

## Bonus
- Try different LoRA `r` values and compare adapter size vs quality.
- Add a self-repair loop that re-prompts when JSON validation fails (Project 6 includes a starting point).

## Resources
See **Day 3** in [../RESOURCES.md](../RESOURCES.md).
