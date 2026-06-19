"""Output guardrails: block restricted content / PII leaks, bound length."""
import re
from dataclasses import dataclass

BANNED = ["password", "credit card number", "social security"]

@dataclass
class OutputCheck:
    allowed: bool
    text: str
    reason: str = ""

def check_output(text: str, max_len: int = 2000) -> OutputCheck:
    if not text or not text.strip():
        return OutputCheck(False, "", "Empty model output")
    if len(text) > max_len:
        text = text[:max_len] + "\u2026"
    low = text.lower()
    if any(b in low for b in BANNED):
        return OutputCheck(False, "", "Output contained restricted content")
    if re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", text):
        return OutputCheck(False, "", "Output contained an email address")
    return OutputCheck(True, text)

SAFE_REFUSAL = ("I can't help with that request. If you believe this is an error, "
                "please rephrase without sensitive details.")
