"""Guardrails reused from Day 7 (trimmed)."""
import re
INJECTION_HINTS = ["ignore previous", "reveal your instructions", "system prompt"]
EMAIL = r"[\w.+-]+@[\w-]+\.[\w.-]+"

def guard_input(text: str):
    if any(h in text.lower() for h in INJECTION_HINTS):
        return False, text, "possible prompt-injection"
    return True, re.sub(EMAIL, "[REDACTED_EMAIL]", text), ""

def guard_output(text: str, contexts: list[str]):
    if not text.strip():
        return False, "empty output"
    if re.search(EMAIL, text):
        return False, "output leaked an email"
    return True, ""
