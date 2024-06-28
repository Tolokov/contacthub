from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.core.engine import session
from app.lib.helpers import successful_message, unsuccessful_message

router = APIRouter()


@router.get('/check_application', summary='Проверка доступности приложения', status_code=200)
async def get_status_application():
    return successful_message


@router.get('/check_database', summary='Проверка доступности базы данных', status_code=200)
async def get_status_database(db: AsyncSession = Depends(session)):
    if await db.connection():
        return successful_message
    else:
        return unsuccessful_message
