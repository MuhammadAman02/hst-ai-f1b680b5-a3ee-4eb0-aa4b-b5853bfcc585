from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME: str = Field("AI Engineer Portfolio", env="APP_NAME")
    APP_VERSION: str = Field("1.0.0", env="APP_VERSION")
    APP_ENV: str = Field("development", env="APP_ENV")
    DEBUG: bool = Field(False, env="DEBUG")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()