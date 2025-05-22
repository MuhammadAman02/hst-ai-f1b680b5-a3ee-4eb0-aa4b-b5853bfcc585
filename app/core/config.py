from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Engineer Portfolio"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = "development"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()