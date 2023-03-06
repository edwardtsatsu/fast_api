from pydantic import BaseSettings


class PostgresConfig(BaseSettings):
    url: str
    user: str
    password: str
    database: str

    class Config:
        env_prefix = "POSTGRES_"
