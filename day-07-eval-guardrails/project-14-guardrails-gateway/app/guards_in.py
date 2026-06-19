"""Input guardrails: reject injection, redact PII before the model/logs see it."""
import re
from dataclasses import dataclass, field

PII_PATTERNS = {
    "email": r"[\w.+-]+@[\w-]+\.[\w.-]+",
    "phone": r"\b(?:\+?\d[\d -]{7,}\d)\b",
    "card":  r"\b(?:\d[ -]?){13,16}\b",
}
INJECTION_HINTS = [
    "ignore previous", "ignore all previous", "disregard the above",
    "you are now", "reveal your system prompt", "reveal your instructions",
    "developer mode",
]

@dataclass
class InputCheck:
    allowed: bool
    cleaned: str
    pii_found: list = field(default_factory=list)
    reason: str = ""

def check_input(text: str) -> InputCheck:
    if len(text) > 4000:
        return InputCheck(False, text, [], "Input too long")
    low = text.lower()
    if any(h in low for h in INJECTION_HINTS):
        return InputCheck(False, text, [], "Possible prompt-injection detected")
    cleaned, found = text, []
    for label, pat in PII_PATTERNS.items():
        if re.search(pat, cleaned):
            found.append(label)
            cleaned = re.sub(pat, f"[REDACTED_{label.upper()}]", cleaned)
    return InputCheck(True, cleaned, found)
