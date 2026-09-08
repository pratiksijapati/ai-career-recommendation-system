# =============================================================
# backend/routes/ml_routes.py
# =============================================================
# PURPOSE:
#   Model performance endpoints -- accuracy, feature importance,
#   per-domain role-model results, and K-Means cluster summaries.
#   This is the evidence trail for the "result analysis" part of
#   the project (and for viva).
# =============================================================

from fastapi import APIRouter
from routes.recommend_routes import get_models

router = APIRouter(prefix="/api/ml", tags=["Model Performance"])


@router.get("/domain-model")
def domain_model_info():
    models = get_models()
    dm = models["domain"]
    return {
        "accuracy": dm["accuracy"],
        "domain_count": len(dm["domain_names"]),
        "domains": dm["domain_names"],
        "top_features": list(dm["importances"].items())[:15],
        "train_samples": dm["train_samples"],
        "test_samples": dm["test_samples"],
        "blend": {
            "note": ("The Domain prediction is a blend of two models, not one -- "
                     "a full-profile model and an interest-only model -- so a "
                     "student's stated interests always carry a guaranteed, "
                     "meaningful weight instead of being drowned out by academic "
                     "score variance."),
            "full_model_accuracy": dm["full_model_accuracy"],
            "interest_model_accuracy": dm["interest_model_accuracy"],
            "interest_blend_weight": dm["blend_weight"],
            "top_interest_features": list(dm["interest_importances"].items())[:5],
        },
    }


@router.get("/role-models")
def role_models_info():
    models = get_models()
    out = []
    for domain, rm in models["roles"].items():
        if rm.get("trained"):
            out.append({
                "domain": domain, "trained": True, "accuracy": rm["accuracy"],
                "role_count": len(rm["role_names"]), "roles": rm["role_names"],
                "train_samples": rm["train_samples"], "test_samples": rm["test_samples"],
            })
        else:
            out.append({"domain": domain, "trained": False, "reason": rm["reason"]})
    return {"role_models": out}


@router.get("/clusters")
def cluster_info():
    models = get_models()
    km = models["kmeans"]
    return {"n_clusters": km["n_clusters"], "clusters": km["summary"]}
