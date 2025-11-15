from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application configuration settings."""
    
    database_url: str = "postgresql://user:password@localhost:5432/mcp_core"
    secret_key: str = "your-secret-key-here"
    debug: bool = True
    allowed_origins: str = "*"
    file_storage_path: str = "./uploads"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
