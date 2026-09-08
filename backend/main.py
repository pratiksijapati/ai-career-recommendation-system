# =============================================================
# backend/main.py — FastAPI Entry Point
# =============================================================

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import explorer_routes, recommend_routes, eda_routes, ml_routes

app = FastAPI(
    title="Career Navigator API",
    version="1.0.0",
    description="Hierarchical (Domain -> Role -> Specialization -> Technology) career recommendation system",
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://localhost:\d+",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(explorer_routes.router)
app.include_router(recommend_routes.router)
app.include_router(eda_routes.router)
app.include_router(ml_routes.router)


@app.get("/")
def root():
    return {
        "message": "Career Navigator API is running!",
        "docs": "Visit /docs for API documentation",
        "endpoints": {
            "explorer": "/api/explorer/taxonomy",
            "recommend_domain": "POST /api/recommend/domain",
            "recommend_role": "POST /api/recommend/role",
            "recommend_specialization": "POST /api/recommend/specialization",
            "skill_gap": "POST /api/recommend/skill-gap",
            "roadmap": "POST /api/recommend/roadmap",
            "eda": "/api/eda/summary",
            "ml": "/api/ml/domain-model",
        },
    }


@app.get("/api/health")
def health_check():
    return {"status": "healthy", "message": "Backend is running"}
