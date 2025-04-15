from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FARM Todo App"
    DEBUG: bool = True

    model_config = {"env_file": ".env"}


settings = Settings()
