from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from app.api.router import router as api_router
from app.config.setting import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    if settings.debug:
        try:
            from app.database.core.engine import delete_tables, create_tables
            # await delete_tables()
            # await create_tables()
            pass
        except ConnectionRefusedError as e:
            print('=== НЕТ БАЗЫ ДАННЫХ ===', end='')
        else:
            print('=== Таблица очищена ===', end='')
        finally:
            print('=== Приложение перезапущено ===')
    yield


app = FastAPI(
    title=settings.title,
    debug=settings.debug,
    root_path=settings.rootPath,
    lifespan=lifespan
)

app.include_router(api_router, prefix='/api')
