from typing import Annotated

from fastapi import Depends, APIRouter

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.core.engine import session
from app.database.models.logs import Logs
from app.api.v1.logging.schemes.logging import LogIn
from app.api.v1.logging.services.logging import LogService

router = APIRouter()


@router.get('/log', summary='Вывести конкретный идентификатор из логов', status_code=200)
async def get_log(id: int = 1, session: AsyncSession = Depends(session)):
    return await LogService(session=session).get(item_id=id)


# @router.get('/log', summary='Выводит сообщение из таблицы логирования', status_code=200)
# async def get_logs(limit: int = 10, db: AsyncSession = Depends(session)):
#     logs = await db.scalars(select(Logs).where(Logs.id != null()).order_by(Logs.id.desc()).limit(limit))
#     return {"logs": logs.all()}, 200


def get_params(message: str, log_level: int = 2, client_level: int = 1):
    return {'log_level': log_level, 'message': message, 'client_level': client_level}


@router.post('/log', summary='Добавить запись в базу данных', status_code=200)
async def post_add_log(
        params: Annotated[LogIn, Depends(LogIn)],
        db: AsyncSession = Depends(session)
) -> {}:
    result = await db.scalar(insert(Logs).values(
        log_level=params.log_level,
        client_level=params.client_level,
        message=params.message
    ).returning(Logs.id))
    await db.commit()
    return {'id': result}, 200
