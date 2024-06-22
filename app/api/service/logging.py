from sqlalchemy import text
from app.database.core.engine import engine

from fastapi import APIRouter

router = APIRouter()


@router.get('/log', summary='Отобразить запись из базы данных', status_code=200)
async def post_add_log():
    result_list = []
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT * FROM logs"))
        for row in result:
            result_list.append(str(row))
        return {"result": result_list}, 200


@router.post('/log', summary='Добавить запись в базу данных', status_code=200)
async def post_add_log(message: str):
    async with engine.begin() as conn:
        query = f"""INSERT INTO logs (log_level, message, timestamp) VALUES ('INFO', '{message}' , '2024-06-22 08:08:08');"""
        print(query)
        await conn.execute(text(query))
    return {'status': message}, 200
