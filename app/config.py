from pydantic_settings import BaseSettings
from functools import lru_cache
from pathlib import Path


data_folder = Path("Users/danielgalvan/Python/test_flask_app/database")


class settings(BaseSettings):
    env: str = "DEV"
    SECRET_KEY: str = ""
    DEBUG: bool = False

    SQLALCHEMY_DATABASE_URI: str = f"sqlite:////{data_folder}/chinook.db"

    class Config:
        env_file: str = ".env"


@lru_cache
def get_settings() -> settings:
    return settings
