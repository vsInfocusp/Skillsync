from pydantic_settings import BaseSettings
from functools import lru_cache
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    APP_ENV: str = os.getenv("APP_ENV", "development")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DATABASE_TEST_URL: str = os.getenv("DATABASE_TEST_URL")

    @property
    def is_testing(self) -> bool:
        return self.APP_ENV == "testing"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
