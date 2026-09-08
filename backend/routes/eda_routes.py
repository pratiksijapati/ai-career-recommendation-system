# =============================================================
# backend/routes/eda_routes.py
# =============================================================
# PURPOSE:
#   Exploratory Data Analysis endpoints -- distributions,
#   relationships, and patterns in the dataset, feeding the
#   frontend's Data Analysis page.
# =============================================================

from fastapi import APIRouter
from modules.data_loader import load_data, get_data_summary, SKILL_COLS, SCORE_COLS

router = APIRouter(prefix="/api/eda", tags=["Data Analysis"])

_df_cache = None


def get_df():
    global _df_cache
    if _df_cache is None:
        _df_cache = load_data()
    return _df_cache


@router.get("/summary")
def summary():
    return get_data_summary(get_df())


@router.get("/domains")
def domain_distribution():
    df = get_df()
    counts = df["domain"].value_counts()
    return {"data": [{"domain": d, "count": int(c), "percentage": round(c / len(df) * 100, 1)}
                      for d, c in counts.items()]}


@router.get("/roles")
def role_distribution():
    df = get_df()
    counts = df.groupby(["domain", "role"]).size().reset_index(name="count")
    return {"data": counts.to_dict(orient="records")}


@router.get("/skills")
def skill_distribution():
    df = get_df()
    by_domain = df.groupby("domain")[SKILL_COLS].mean().round(2)
    return {"data": by_domain.reset_index().to_dict(orient="records")}


@router.get("/scores")
def score_distribution():
    df = get_df()
    by_domain = df.groupby("domain")[SCORE_COLS].mean().round(1)
    return {"data": by_domain.reset_index().to_dict(orient="records")}


@router.get("/education")
def education_distribution():
    df = get_df()
    counts = df["education_level"].value_counts()
    return {"data": [{"education_level": e, "count": int(c)} for e, c in counts.items()]}


@router.get("/correlation")
def correlation():
    df = get_df()
    corr = df[SKILL_COLS + SCORE_COLS].corr().round(2)
    return {"columns": corr.columns.tolist(), "matrix": corr.values.tolist()}
