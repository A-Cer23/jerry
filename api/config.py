from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: str = "local"
    db_user: str = "admin"
    db_password: str = "password"
    db_host: str = "0.0.0.0"
    db_port: int = 5432
    db_name: str = "jerry_api_db"

    def get_db_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()