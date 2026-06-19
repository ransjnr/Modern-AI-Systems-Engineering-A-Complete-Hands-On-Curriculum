# Day 2 — RAG & Vector Databases

Ground LLM answers in your own documents. Learn embeddings, chunking, retrieval, and the RAG pipeline.

## Projects
| # | Project | Folder | Stack |
|---|---------|--------|-------|
| 3 | Medical Literature RAG | `project-03-medical-rag/` | OpenAI embeddings · vector search · FastAPI |
| 4 | Product Recommender | `project-04-product-recommender/` | embeddings · cosine similarity |

## Keys needed
`OPENAI_API_KEY` (required). `PINECONE_API_KEY` (optional — Project 3 includes an in-memory store so it runs with zero extra infra).

## Learning objectives
- Turn text into embeddings; store and search by similarity.
- Chunk documents sensibly; build a retrieve→augment→generate pipeline.
- Understand naive vs advanced RAG (hybrid search, re-ranking).

## Bonus challenges
- Swap the in-memory store for Pinecone or pgvector.
- Add a cross-encoder re-ranker over the top-k results.
- Add citations: return which chunk each fact came from.

## Resources
See **Day 2 — RAG** in [../RESOURCES.md](../RESOURCES.md).
