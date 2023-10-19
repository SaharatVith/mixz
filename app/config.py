from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_username: str = "postgres"
    database_password: str = "root"
    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "travel_bkk"
    secret_key: str = "saiodfjsioa"
    algorithm: str = "HS256"
    access_token_exprie_minutes: int = 90


settings = Settings()
