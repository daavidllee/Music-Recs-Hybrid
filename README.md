# Music Recommendation Engine (Hybrid: CF + Neural Embeddings)

**What it is:** A hybrid recommender that blends collaborative filtering with neural track embeddings derived from Spotify audio features. Ranks candidates using a gradient-boosted ranker and evaluates with MAP and NDCG.

## Why this matters (Spotify Personalization)
- Hybrid approach reflects production systems that combine CF signals with content embeddings.
- Clear offline eval (MAP/NDCG) + ranker training mirrors ranking stacks used in large-scale recommenders.
- Includes a minimal API to surface top-N recommendations for a user or seed track list.

## Tech Stack
Python, Pandas, NumPy, scikit-learn, TensorFlow/PyTorch (embeddings), XGBoost, FastAPI, Uvicorn.

## Repo Structure (initial)
- `src/api/app.py` — minimal FastAPI service with `/health` + `/recommend`
- `src/eval/metrics.py` — MAP@K & NDCG@K
- `src/eval/offline_eval.py` — tiny demo runner
- `requirements.txt`, `.gitignore`, `docs/` placeholders
- `data/.gitkeep`, `notebooks/.gitkeep`

## Next steps
1) Add Spotify data fetching (`src/data/fetch_spotify.py`)
2) Train embeddings + CF baseline
3) Add ranker + offline eval, log MAP/NDCG in `docs/results.md`
# Music-Recs-Hybrid
