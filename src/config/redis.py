from pydantic import BaseSettings


class RedisConfig(BaseSettings):
    url: str
    db: int = 0

    class Config:
        env_prefix = "REDIS_"
