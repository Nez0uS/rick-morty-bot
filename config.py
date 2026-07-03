from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Telegram
    bot_token: str

    # Rick and Morty API
    api_base_url: str = "https://rickandmortyapi.com/api"

    # Database
    db_url: str = "sqlite+aiosqlite:///./rick_morty.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()