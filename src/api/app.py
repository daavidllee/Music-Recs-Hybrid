from fastapi import FastAPI, Query
from typing import List

app = FastAPI(title="music-recs-hybrid", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/recommend")
def recommend(user_id: str | None = Query(None), seed_tracks: List[str] | None = Query(None), k: int = 10):
    # TODO: wire up candidate generation + ranker; return dummy for now
    recs = [f"track_{i}" for i in range(1, k+1)]
    return {"user_id": user_id, "seed_tracks": seed_tracks, "recommendations": recs}
