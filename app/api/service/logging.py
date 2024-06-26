from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.core.engine import engine
from fastapi import Depends
from app.database.core.engine import session
from app.database.models.logs import Logs
from fastapi import APIRouter
from sqlalchemy import select, null

router = APIRouter()


@router.get('/log', summary='Выводит сообщение из таблицы логирования', status_code=200)
async def get_logs(db: AsyncSession = Depends(session)):
    logs = await db.scalars(select(Logs).where(Logs.id != null()).order_by(Logs.timestamp))
    return {"result": logs.all()}, 200


@router.post('/log', summary='Добавить запись в базу данных', status_code=200)
async def post_add_log(message: str):
    async with engine.begin() as conn:
        query = f"""INSERT INTO logs (log_level, message, timestamp) VALUES ('INFO', '{message}' , '2024-06-22 08:08:08');"""
        print(query)
        await conn.execute(text(query))
    return {'status': message}, 200
