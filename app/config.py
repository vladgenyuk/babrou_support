import sys

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env-tests" if "pytest" in sys.modules else ".env"
        env_file_encoding = "utf-8"


settings = Settings()
