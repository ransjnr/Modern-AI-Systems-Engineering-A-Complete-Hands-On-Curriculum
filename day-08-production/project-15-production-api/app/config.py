"""Environment-based settings. Fails fast if a required var is missing."""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    redis_url: str = "redis://localhost:6379/0"
    model: str = "gpt-4o-mini"
    request_timeout_s: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
