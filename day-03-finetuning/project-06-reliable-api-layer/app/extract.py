"""Force the LLM to return a validated SupportTicket via function calling + retry."""
import json
from openai import OpenAI
from pydantic import ValidationError
from tenacity import retry, stop_after_attempt, wait_fixed
from app.schemas import SupportTicket

client = OpenAI()
MODEL = "gpt-4o-mini"

TOOL = {
    "type": "function",
    "function": {
        "name": "create_ticket",
        "description": "Create a structured support ticket from the message.",
        "parameters": SupportTicket.model_json_schema(),
    },
}

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def extract_ticket(text: str) -> SupportTicket:
    resp = client.chat.completions.create(
        model=MODEL, temperature=0,
        messages=[
            {"role": "system", "content":
             "Extract a support ticket. Use 'unknown' for missing fields."},
            {"role": "user", "content": text},
        ],
        tools=[TOOL],
        tool_choice={"type": "function", "function": {"name": "create_ticket"}},
    )
    call = resp.choices[0].message.tool_calls[0]
    args = json.loads(call.function.arguments)
    # Validates here; on ValidationError tenacity retries the whole call.
    return SupportTicket.model_validate(args)
