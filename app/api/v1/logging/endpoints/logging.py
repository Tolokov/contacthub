from typing import Annotated

from fastapi import Depends, APIRouter, status
from fastapi_filter.base.filter import FilterDepends

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.core.engine import session
from app.database.models.logs import Logs
from app.api.v1.logging.schemes.logging import LogIn, LogFilter, LogResponse, LogInResponse
from app.api.v1.logging.services.logging import LogService

router = APIRouter()


@router.get(
    '/log',
    summary='Вывести логи',
    status_code=status.HTTP_200_OK,
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
    status_code=status.HTTP_200_OK,
    response_model=LogInResponse,
    description="Засылаем сюда логи"
)
async def post_add_log(
        params: Annotated[LogIn, Depends(LogIn)],
        session: AsyncSession = Depends(session)
) -> {"id": LogInResponse}:
    return {"id": await LogService(session=session).post(params)}
