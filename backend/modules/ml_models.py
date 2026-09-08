# =============================================================
# backend/modules/ml_models.py
# =============================================================
# PURPOSE:
#   Train the hierarchical recommendation pipeline:
#
#   Level 1 (Domain)          -> Random Forest, trained on the
#                                 whole dataset. Real aptitude signal
#                                 exists here (skills/academics
#                                 genuinely relate to domain fit).
#
#   Level 2 (Role)            -> One Random Forest PER DOMAIN
#                                 (a cascade), each trained only on
#                                 that domain's students. Fewer
#                                 competing classes + more relevant
#                                 training data than one flat model.
#
#   Level 3 (Specialization)  -> NOT a trained classifier. There is
#                                 no honest ground truth linking
#                                 academic scores to "will you prefer
#                                 Web vs Mobile development" -- that's
#                                 driven by exposure and curiosity,
#                                 not aptitude. Instead: find the most
#                                 similar real students within that
#                                 role (KNN) and report which
#                                 specializations THEY actually chose,
#                                 as a similarity-based relevance
#                                 score, not a fabricated prediction.
#
#   K-Means                   -> Unsupervised student-archetype
#                                 clustering, for EDA/insight only --
#                                 not part of the recommendation path.
# =============================================================

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report

from modules.data_loader import (
    load_data, DOMAIN_FEATURE_COLS, DOMAIN_AGG_COLS, ROLE_BASE_FEATURE_COLS,
    INTEREST_TAXONOMY,
)

# How much the interest-only signal counts in the final Domain blend.
# See the design note on train_domain_model() for why this exists.
INTEREST_BLEND_WEIGHT = 0.45


# =============================================================
# LEVEL 1 — DOMAIN MODEL
# =============================================================
# Trained as TWO models blended together, not one:
#   - a full-profile Random Forest (academics + skills + prefs + interests)
#   - an interest-only Random Forest (just the interest-domain aggregates)
# Why: academic scores have much bigger between-domain spread (e.g.
# business_score averages ~92 in Finance vs ~62 in Technology) than
# interest tags do, so in one shared model, score features end up
# dominating every split and interests barely move the outcome --
# meaning a student who leaves academics at the wizard's defaults and
# only sets interests gets a result driven by "average student," not
# by what they actually told the system about themselves. Blending in
# a dedicated interest-only model guarantees interests always get a
# real, guaranteed say, the same way the sister project blends RF+KNN
# with a stated weight rather than leaving it to chance.

def train_domain_model(df: pd.DataFrame) -> dict:
    y = df["domain"].values
    le = LabelEncoder()
    y_enc = le.fit_transform(y)

    # Single shared split so both models are evaluated on the same
    # held-out students and their predict_proba columns line up
    idx_train, idx_test = train_test_split(
        df.index.values, test_size=0.2, random_state=42, stratify=y_enc
    )
    y_train, y_test = y_enc[idx_train], y_enc[idx_test]

    def _train_one(feature_cols, n_estimators, max_depth):
        X = df[feature_cols].values
        X_train, X_test = X[idx_train], X[idx_test]
        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)

        # class_weight='balanced' matters a lot here: domains with
        # specialization depth (Technology, Finance, Design) end up
        # with far more training rows than shallow domains, purely as
        # a side effect of the Level-3 oversampling -- without this,
        # the model learns a population-size prior and defaults to
        # the biggest domains whenever the real signal is weak/mixed,
        # regardless of what the student actually said.
        rf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth,
                                     class_weight='balanced', random_state=42)
        rf.fit(X_train_s, y_train)

        acc = accuracy_score(y_test, rf.predict(X_test_s))
        importances = dict(sorted(
            zip(feature_cols, rf.feature_importances_.tolist()),
            key=lambda x: x[1], reverse=True
        ))
        return rf, scaler, acc, importances

    full_rf, full_scaler, full_acc, full_importances = _train_one(
        DOMAIN_FEATURE_COLS, n_estimators=200, max_depth=12)
    interest_rf, interest_scaler, interest_acc, interest_importances = _train_one(
        DOMAIN_AGG_COLS, n_estimators=150, max_depth=8)

    # Blended accuracy, evaluated the same honest way as each individual model
    full_probs_test = full_rf.predict_proba(full_scaler.transform(df[DOMAIN_FEATURE_COLS].values[idx_test]))
    interest_probs_test = interest_rf.predict_proba(interest_scaler.transform(df[DOMAIN_AGG_COLS].values[idx_test]))
    blended_probs_test = (1 - INTEREST_BLEND_WEIGHT) * full_probs_test + INTEREST_BLEND_WEIGHT * interest_probs_test
    blended_acc = accuracy_score(y_test, blended_probs_test.argmax(axis=1))

    return {
        "model": full_rf, "scaler": full_scaler,
        "interest_model": interest_rf, "interest_scaler": interest_scaler,
        "label_encoder": le,
        "feature_cols": DOMAIN_FEATURE_COLS,
        "interest_feature_cols": DOMAIN_AGG_COLS,
        "blend_weight": INTEREST_BLEND_WEIGHT,
        "accuracy": round(blended_acc * 100, 2),
        "full_model_accuracy": round(full_acc * 100, 2),
        "interest_model_accuracy": round(interest_acc * 100, 2),
        "domain_names": le.classes_.tolist(),
        "importances": full_importances,
        "interest_importances": interest_importances,
        "train_samples": len(idx_train), "test_samples": len(idx_test),
    }


# =============================================================
# LEVEL 2 — ROLE MODELS (one per domain, the actual "cascade")
# =============================================================

def train_role_models(df: pd.DataFrame) -> dict:
    role_models = {}

    for domain in df["domain"].unique():
        sub = df[df["domain"] == domain]
        feature_cols = ROLE_BASE_FEATURE_COLS + INTEREST_TAXONOMY[domain]

        n_classes = sub["role"].nunique()
        if n_classes < 2 or len(sub) < n_classes * 10:
            # Not enough data to honestly train/evaluate a classifier here
            role_models[domain] = {"trained": False, "reason": "insufficient data"}
            continue

        X = sub[feature_cols].values
        y = sub["role"].values

        le = LabelEncoder()
        y_enc = le.fit_transform(y)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y_enc, test_size=0.2, random_state=42, stratify=y_enc
        )

        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)

        rf = RandomForestClassifier(n_estimators=150, max_depth=10, random_state=42)
        rf.fit(X_train_s, y_train)

        y_pred = rf.predict(X_test_s)
        acc = accuracy_score(y_test, y_pred)

        role_models[domain] = {
            "trained": True,
            "model": rf, "scaler": scaler, "label_encoder": le,
            "feature_cols": feature_cols,
            "accuracy": round(acc * 100, 2),
            "role_names": le.classes_.tolist(),
            "train_samples": len(X_train), "test_samples": len(X_test),
        }

    return role_models


# =============================================================
# LEVEL 3 — SPECIALIZATION (similarity-based, not a classifier)
# =============================================================

def recommend_specializations(student_vector: np.ndarray, domain: str, role: str,
                                df: pd.DataFrame, k: int = 15) -> list:
    """
    Find the K most similar profiles in the dataset who chose this
    exact Role, and report which Specializations THEY chose, ranked by
    how often they appear among the neighbors. This is deliberately
    similarity-based rather than a trained classifier -- there's no
    honest way to claim a model "predicted" a specialization choice
    from academic scores alone, so we report nearest-neighbor evidence
    from the dataset instead.

    Returns:
        list of {specialization, relevance_pct, supporting_students}
        or [] if this role has no specializations.
    """
    role_df = df[(df["domain"] == domain) & (df["role"] == role) & (df["specialization"] != "")]
    if role_df.empty:
        return []

    feature_cols = ROLE_BASE_FEATURE_COLS
    X = role_df[feature_cols].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    query_scaled = scaler.transform(student_vector.reshape(1, -1))

    n_neighbors = min(k, len(role_df))
    nn = NearestNeighbors(n_neighbors=n_neighbors)
    nn.fit(X_scaled)
    _, indices = nn.kneighbors(query_scaled)

    neighbor_specs = role_df.iloc[indices[0]]["specialization"]
    counts = neighbor_specs.value_counts()

    results = []
    for spec, count in counts.items():
        results.append({
            "specialization": spec,
            "relevance_pct": round(count / n_neighbors * 100, 1),
            "supporting_students": int(count),
        })
    results.sort(key=lambda x: x["relevance_pct"], reverse=True)
    return results


# =============================================================
# K-MEANS — student archetypes (EDA / insight only)
# =============================================================

def train_kmeans(df: pd.DataFrame, n_clusters: int = 6) -> dict:
    from modules.data_loader import SKILL_COLS  # local import to avoid cycle at module load

    X = df[SKILL_COLS].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    km = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)

    df_c = df.copy()
    df_c["cluster"] = labels

    summary = []
    for i in range(n_clusters):
        cluster_df = df_c[df_c["cluster"] == i]
        summary.append({
            "cluster_id": i,
            "student_count": int(len(cluster_df)),
            "avg_skills": cluster_df[SKILL_COLS].mean().round(2).to_dict(),
            "top_domains": cluster_df["domain"].value_counts().head(3).to_dict(),
        })

    return {"model": km, "scaler": scaler, "cluster_labels": labels.tolist(),
            "n_clusters": n_clusters, "summary": summary}


# =============================================================
# TRAIN EVERYTHING
# =============================================================

def train_all_models() -> dict:
    df = load_data()
    domain_model = train_domain_model(df)
    role_models = train_role_models(df)
    kmeans = train_kmeans(df)

    return {
        "df": df,
        "domain": domain_model,
        "roles": role_models,
        "kmeans": kmeans,
    }


if __name__ == "__main__":
    models = train_all_models()
    print(f"Domain model accuracy: {models['domain']['accuracy']}%")
    print(f"Domain classes: {len(models['domain']['domain_names'])}")
    print("\nTop 10 domain feature importances:")
    for feat, imp in list(models["domain"]["importances"].items())[:10]:
        print(f"  {feat:35s} {imp:.4f}")

    print("\nRole model accuracy per domain:")
    for domain, rm in models["roles"].items():
        if rm.get("trained"):
            print(f"  {domain:35s} {rm['accuracy']}% ({len(rm['role_names'])} roles, "
                  f"{rm['train_samples']}+{rm['test_samples']} samples)")
        else:
            print(f"  {domain:35s} SKIPPED ({rm['reason']})")
