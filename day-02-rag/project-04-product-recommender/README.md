# Project 4 — Personalised Product Recommender (Vector Similarity)

Recommend products by embedding a user's interest text and finding the most similar
products by cosine similarity — the same vector-search idea behind RAG, applied to
recommendations.

## Run
```bash
pip install openai numpy fastapi uvicorn pydantic python-dotenv
python app/build_index.py        # embeds data/products.json
uvicorn app.main:app --reload
```
```bash
curl -X POST localhost:8000/recommend -H 'Content-Type: application/json' \
  -d '{"interest":"lightweight running shoes for marathons","k":3}'
```

## Bonus
- Add category filters before similarity ranking.
- Blend popularity score with similarity (hybrid ranking).
