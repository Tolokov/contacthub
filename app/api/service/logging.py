from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends
from app.database.core.engine import session
from app.database.models.logs import Logs
from fastapi import APIRouter
from sqlalchemy import select, null, insert

router = APIRouter()


@router.get('/log', summary='Выводит сообщение из таблицы логирования', status_code=200)
async def get_logs(limit: int = 10, db: AsyncSession = Depends(session)):
    logs = await db.scalars(select(Logs).where(Logs.id != null()).order_by(Logs.id.desc()).limit(limit))
    return {"logs": logs.all()}, 200


# class LogSchema(BaseModel):
#     message: str
#     log_level: LoggerLevel
#     client_level: ClientLevel

@router.post('/log', summary='Добавить запись в базу данных', status_code=200)
async def post_add_log(message: str, log_level: int = 2, client_level: int = 1, db: AsyncSession = Depends(session)):
    result = await db.scalar(insert(Logs).values(
        log_level=log_level,
        client_level=client_level,
        message=message
    ).returning(Logs.id))
    await db.commit()
    return {'id': result}, 200
