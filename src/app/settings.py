from pydantic import BaseSettings
from pathlib import Path

BASE_DIR = 'src'
ABS_BASE_DIR = str([p for p in Path(__file__).absolute().parents if p.name == BASE_DIR][0])


class SecretSettings(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_port: str


secret_settings = SecretSettings(
    _env_file=f'{ABS_BASE_DIR}/.envs/.env',
    _env_file_encoding='utf-8',
)


class Settings(BaseSettings):
    server_host: str = '0.0.0.0'
    server_port: int = 8000
    database_url: str = f'postgresql+asyncpg://{secret_settings.postgres_user}:{secret_settings.postgres_password}' \
                        f'@{server_host}:{secret_settings.postgres_port}/{secret_settings.postgres_db}'


settings = Settings()
