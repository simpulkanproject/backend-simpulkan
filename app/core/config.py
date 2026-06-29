from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "SimpulkanProject"
    app_version: str = "0.1.0"
    app_env: str = "development"


settings = Settings()
