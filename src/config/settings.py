from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My Project"
    debug: bool = False
    database_url: str = "postgresql://user:postgrees@localhost/postgres"
    redis_url: str = "redis://localhost:6379"

settings = Settings()
