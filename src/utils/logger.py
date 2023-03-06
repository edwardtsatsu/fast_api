from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My FastAPI App"
    app_description: str = "A cool FastAPI app"
    log_level: str = "debug"
    database_url: str
    redis_url: str

    class Config:
        env_file = ".env"
        env_prefix = "MYAPP_"
