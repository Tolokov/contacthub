from typing import Annotated

from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from fastapi_filter.base.filter import FilterDepends

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.core.engine import session
from app.database.models.logs import Logs

from app.api.v1.logging.schemes.logging import LogIn, LogFilter, LogResponse, LogInResponse
from app.api.v1.logging.services.logging import LogService

router = APIRouter()


@router.get(
    '/log',
    summary='Вывести логи',
    status_code=200,
    response_model=list[LogResponse]
)
async def get_log(
        filters: Annotated[LogFilter, FilterDepends(LogFilter)],
        session: AsyncSession = Depends(session)
) -> list[Logs]:
    return await LogService(session=session).get(filters)


@router.post(
    '/log',
    summary='Добавить запись в базу данных',
    status_code=200,
    response_model=LogInResponse
)
async def post_add_log(
        params: Annotated[LogIn, Depends(LogIn)],
        db: AsyncSession = Depends(session)
) -> LogInResponse:
    result = await db.scalar(insert(Logs).values(
        log_level=params.log_level,
        client_level=params.client_level,
        message=params.message
    ).returning(Logs.id))
    await db.commit()
    return {'id': result}
