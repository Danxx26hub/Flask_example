from pydantic_settings import BaseSettings
from functools import lru_cache
from pathlib import Path


data_folder = Path("Users/danielgalvan/Python/test_flask_app/database")


class prod_settings(BaseSettings):
    """prod settings"""
    env: str = "prod"
    SECRET_KEY: str = ""
    DEBUG: bool = False
    db_name: str = "chinook.db"
    SQLALCHEMY_DATABASE_URI: str = f"sqlite:////{data_folder}/{db_name}"
    CACHE_TYPE: str = 'SimpleCache'
    FLASK_ADMIN_SWATCH: str = 'cerulean'

    class Config:
        """config class for local secrets"""
        env_file: str = ".env"


class dev_settings(BaseSettings):
    """dev settings"""
    env: str = "DEV"
    SECRET_KEY: str = ""
    DEBUG: bool = True
    db_name: str = "chinook.db"
    SQLALCHEMY_DATABASE_URI: str = f"sqlite:////{data_folder}/{db_name}"
    CACHE_TYPE: str = 'FileSystemCache'
    CACHE_DIR: str = 'cache/flask_cache'
    FLASK_ADMIN_SWATCH: str = 'cerulean'
    class Config:
        env_file: str = ".PRODenv"


@lru_cache
def get_settings(env):
    if env == "dev":
        settings = dev_settings

    else:
        settings = prod_settings
    return settings
