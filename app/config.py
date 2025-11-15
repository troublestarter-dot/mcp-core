from pydantic_settings import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    APP_NAME: str = "mcp-core"
    ENV: str = "production"
    PORT: int = 10000
    # Пример: "https://example.com,https://another.com"
    CORS_ORIGINS: Optional[List[str]] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
