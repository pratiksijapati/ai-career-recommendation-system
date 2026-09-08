# =============================================================
# backend/routes/explorer_routes.py
# =============================================================
# PURPOSE:
#   Career Explorer -- pure browsing, no ML, no student profile
#   needed. Directly answers "students don't know these careers
#   exist" independent of any quiz result.
# =============================================================

from fastapi import APIRouter
from career_taxonomy import CAREER_TAXONOMY, flatten_roles, flatten_specializations
from interest_taxonomy import INTEREST_TAXONOMY

router = APIRouter(prefix="/api/explorer", tags=["Career Explorer"])


@router.get("/taxonomy")
def get_taxonomy():
    """Full Domain -> Role -> Specialization -> Technology tree."""
    return {"taxonomy": CAREER_TAXONOMY}


@router.get("/domains")
def list_domains():
    return {
        "domains": [
            {"name": name, "role_count": len(data["roles"]),
             "expandable": data.get("expandable", False)}
            for name, data in CAREER_TAXONOMY.items()
        ]
    }


@router.get("/domains/{domain}/roles")
def list_roles(domain: str):
    ddata = CAREER_TAXONOMY.get(domain)
    if not ddata:
        return {"error": f"Unknown domain: {domain}"}
    return {
        "domain": domain,
        "roles": [
            {"name": role, "specialization_count": len(rdata.get("specializations", {}))}
            for role, rdata in ddata["roles"].items()
        ],
    }


@router.get("/domains/{domain}/roles/{role}/specializations")
def list_specializations(domain: str, role: str):
    rdata = CAREER_TAXONOMY.get(domain, {}).get("roles", {}).get(role)
    if rdata is None:
        return {"error": f"Unknown role: {role} in {domain}"}

    specs = []
    for spec, sdata in rdata.get("specializations", {}).items():
        if "sub_specializations" in sdata:
            for sub, subdata in sdata["sub_specializations"].items():
                specs.append({
                    "name": f"{spec} — {sub}",
                    "technologies": subdata.get("technologies", []),
                })
        else:
            specs.append({"name": spec, "technologies": sdata.get("technologies", [])})

    return {"domain": domain, "role": role, "specializations": specs}


@router.get("/interests")
def get_interest_taxonomy():
    """Interest-tag vocabulary for the profile-builder's tag picker."""
    return {"interest_taxonomy": INTEREST_TAXONOMY}
