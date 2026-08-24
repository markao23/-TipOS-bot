from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    discord_token: str
    database_url: str
    environment: str = "development"
    model_config = SettingsConfigDict(env_file=".env", enable_decoding="utf-8")

settings = Settings()