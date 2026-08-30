from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    discord_token: str
    database_url: str
    environment: str = "development"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()