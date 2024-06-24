from pydantic import computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    title: str = 'ContactHub'
    version: str = '0.1c'

    host: str = '127.0.0.1'
    port: int = 8080

    debug: bool | None = False
    loger: bool | None = False

    rootPath: str = f'http://{host}:{port}/'
    dbDialect: str = 'postgresql+asyncpg'

    dbUser: str = 'postgres'
    dbPass: str = 'postgres'
    dbHost: str = 'localhost'
    dbPort: int = 5432
    dbName: str = 'postgres'

    secretKey: str = 'hi hackerman 😘'

    @computed_field
    @property
    def db_url(self) -> str:
        return f'{self.dbDialect}://{self.dbUser}:{self.dbPass}@{self.dbHost}:{self.dbPort}/{self.dbName}'


settings = Settings()
