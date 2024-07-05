from typing import Generic, TypeVar

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.core.base import BaseModel
from app.database.repositories.base import BaseRepository

TModel = TypeVar('TModel', bound=BaseModel)


class SqlalchemyRepository(BaseRepository, Generic[TModel]):
    model: type[TModel]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, item_id: int, lazy: bool = False) -> TModel:
        query = select(self.model).filter(getattr(self.model, 'id') == item_id).order_by(getattr(self.model, 'id'))
        return await self.session.scalar(query)

    async def post(self, data: dict, lazy: bool = False) -> TModel:
        query = insert(self.model).values(data).returning(getattr(self.model, 'id'))
        instance = await self.session.scalar(query)
        await self.session.commit()
        return instance


class ModelRepository(SqlalchemyRepository, Generic[TModel]):
    def __init__(self, session: AsyncSession, model: type[TModel]):
        self.model = model
        super().__init__(session)
