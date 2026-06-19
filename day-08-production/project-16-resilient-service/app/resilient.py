"""Retry + timeout + circuit-breaker fallback around the model call."""
import os
from tenacity import (retry, wait_exponential, stop_after_attempt,
                      retry_if_exception_type)
from openai import AsyncOpenAI, APIError, APITimeoutError, RateLimitError

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"), timeout=20)

@retry(wait=wait_exponential(multiplier=1, max=8), stop=stop_after_attempt(3),
       retry=retry_if_exception_type((APIError, APITimeoutError, RateLimitError)))
async def _call(model: str, prompt: str) -> str:
    r = await client.chat.completions.create(
        model=model, messages=[{"role": "user", "content": prompt}])
    return r.choices[0].message.content

async def resilient_answer(prompt: str) -> dict:
    try:
        return {"answer": await _call("gpt-4o", prompt), "source": "primary"}
    except Exception:
        try:
            return {"answer": await _call("gpt-4o-mini", prompt), "source": "fallback-mini"}
        except Exception:
            return {"answer": "Service is busy right now - please retry shortly.",
                    "source": "fallback-canned"}
