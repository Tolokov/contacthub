from fastapi import APIRouter

from app.lib.helpers import successful_message, unsuccessful_message

router = APIRouter()


@router.get('/check_application', summary='Проверка доступности приложения', status_code=200)
async def get_status_application():
    return successful_message


@router.get('/check_database', summary='Проверка доступности базы данных', status_code=200)
async def get_status_database():
    from app.database.core.engine import engine
    from sqlalchemy import text
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT * FROM logs")).all()
        print(f"{res}")
    if res:
        return successful_message
    else:
        return unsuccessful_message


