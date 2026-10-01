
import os
import sys
import pandas as pd
import numpy as np

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
sys.path.insert(0, DATA_DIR)  # so we can import career_taxonomy / interest_taxonomy / generate_data

from career_taxonomy import CAREER_TAXONOMY, flatten_roles, flatten_specializations  # noqa: E402
from interest_taxonomy import INTEREST_TAXONOMY, all_tags, tag_to_domain  # noqa: E402
from generate_data import SKILL_COLS, SCORE_COLS, PREFERENCE_COLS, TOOL_COLS  # noqa: E402

DATA_PATH = os.path.join(DATA_DIR, "career_data.csv")

INTEREST_TAGS = all_tags()
TAG_TO_DOMAIN = tag_to_domain()

DOMAIN_AGG_COLS = [f"interest_agg__{d}" for d in INTEREST_TAXONOMY.keys()]
DOMAIN_FEATURE_COLS = SKILL_COLS + SCORE_COLS + PREFERENCE_COLS + DOMAIN_AGG_COLS


ROLE_BASE_FEATURE_COLS = SKILL_COLS + SCORE_COLS + PREFERENCE_COLS


def load_data() -> pd.DataFrame:
    """Load the CSV, clean it, and add the domain-interest aggregate columns."""
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            f"Dataset not found at: {DATA_PATH}\nRun: python generate_data.py first"
        )

    df = pd.read_csv(DATA_PATH)
    df = _clean(df)
    df = _add_domain_aggregates(df)
    return df


def _clean(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip()
    df.drop_duplicates(inplace=True)

    for col in SKILL_COLS + PREFERENCE_COLS:
        if col in df.columns:
            df[col] = df[col].clip(1, 5)
    for col in SCORE_COLS:
        if col in df.columns:
            df[col] = df[col].clip(0, 100)
    for col in INTEREST_TAGS:
        if col in df.columns:
            df[col] = df[col].clip(0, 3)
    for col in TOOL_COLS:
        if col in df.columns:
            df[col] = df[col].clip(0, 5)

    df["specialization"] = df["specialization"].fillna("")
    return df


def _add_domain_aggregates(df: pd.DataFrame) -> pd.DataFrame:
    """
    For each Interest Domain, sum the strengths of its tags into one
    aggregate column. This is what feeds the coarse Level-1 model --
    the raw 78 tags are too sparse for a reliable domain-level signal,
    but "how much, in total, does this student lean toward Sports-
    related tags" is a clean, dense feature.
    """
    agg_cols = {}
    for domain, tags in INTEREST_TAXONOMY.items():
        present_tags = [t for t in tags if t in df.columns]
        agg_cols[f"interest_agg__{domain}"] = df[present_tags].sum(axis=1)
    return pd.concat([df, pd.DataFrame(agg_cols, index=df.index)], axis=1)


def get_data_summary(df: pd.DataFrame) -> dict:
    return {
        "total_students": int(len(df)),
        "total_features": int(len(df.columns)),
        "domain_count": int(df["domain"].nunique()),
        "role_count": int(df["role"].nunique()),
        "specialization_count": int(df[df["specialization"] != ""]["specialization"].nunique()),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "domain_distribution": df["domain"].value_counts().to_dict(),
        "education_distribution": df["education_level"].value_counts().to_dict(),
        "gender_distribution": df["gender"].value_counts().to_dict(),
    }
