from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.core.engine import engine
from fastapi import Depends
from app.database.core.engine import session
from app.database.models.logs import Logs
from fastapi import APIRouter
from sqlalchemy import select, null, insert
router = APIRouter()


@router.get('/log', summary='Выводит сообщение из таблицы логирования', status_code=200)
async def get_logs(db: AsyncSession = Depends(session)):
    logs = await db.scalars(select(Logs).where(Logs.id != null()).order_by(Logs.timestamp))
    return {"logs": logs.all()}, 200


@router.post('/log', summary='Добавить запись в базу данных', status_code=200)
async def post_add_log(message: str, db: AsyncSession = Depends(session)):
    result = await db.scalar(insert(Logs).values(message=message).returning(Logs.id))
    await db.commit()
    return {'id': result}, 200
