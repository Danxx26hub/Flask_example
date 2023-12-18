from pydantic_settings import BaseSettings
from functools import lru_cache
from pathlib import Path


data_folder = Path("Users/danielgalvan/Python/test_flask_app/database")


class prod_settings(BaseSettings):
    env: str = "prod"
    SECRET_KEY: str = ""
    DEBUG: bool = False
    db_name: str = "chinook.db"
    SQLALCHEMY_DATABASE_URI: str = f"sqlite:////{data_folder}/{db_name}"

    class Config:
        env_file: str = ".env"


class dev_settings(BaseSettings):
    env: str = "DEV"
    SECRET_KEY: str = ""
    DEBUG: bool = True
    db_name: str = "chinook.db"
    SQLALCHEMY_DATABASE_URI: str = f"sqlite:////{data_folder}/{db_name}"

    class Config:
        env_file: str = ".PRODenv"


@lru_cache
def get_settings(env):
    if env == "dev":
        settings = dev_settings

    else:
        settings = prod_settings
    return settings
