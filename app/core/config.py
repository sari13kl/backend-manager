from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "Task Manager"
    ENVIRONMENT: str = Field(default="development")
    
    DATABASE_URL: str
    
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()