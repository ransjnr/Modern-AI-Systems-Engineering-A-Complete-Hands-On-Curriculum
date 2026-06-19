"""Curated, conservative symptom-reference tool (stand-in for a vetted clinical API)."""
from crewai.tools import tool

SYMPTOM_REFERENCE = {
    "chest pain": {"common_context": ["muscle strain", "acid reflux", "anxiety"],
                   "red_flags": ["crushing pain", "pain to arm/jaw", "shortness of breath",
                                 "cold sweat"], "urgency": "HIGH"},
    "headache": {"common_context": ["tension", "dehydration", "eye strain", "migraine"],
                 "red_flags": ["sudden worst-ever headache", "fever + stiff neck",
                               "confusion", "one-sided weakness"], "urgency": "MODERATE"},
    "abdominal pain": {"common_context": ["indigestion", "gas", "muscle strain"],
                       "red_flags": ["rigid abdomen", "vomiting blood", "fainting"],
                       "urgency": "MODERATE"},
}

@tool("Symptom Reference Lookup")
def symptom_reference(symptom: str) -> str:
    """Return vetted context and recognised red-flags for a symptom. If unknown, say so
    explicitly rather than inventing information."""
    key = symptom.lower().strip()
    for name, data in SYMPTOM_REFERENCE.items():
        if name in key or key in name:
            return str({"symptom": name, **data})
    return f"No curated reference for '{symptom}'. State this gap and recommend a clinician."
