from app.database.core.base import BaseModel
from typing import Generic, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.services.base import BaseService
from app.lib.exceptions import DoesNotExist

from app.database.repositories.sqlalchemy_repository import ModelRepository
TModel = TypeVar('TModel', bound=BaseModel)


class SqlalchemyService(BaseService, Generic[TModel]):
    model: type[TModel]

    def __init__(self, session: AsyncSession):
        self.repository = ModelRepository[TModel](session=session, model=self.model)

    # async def get(self):
    #     return await ''

    async def get(self, item_id: int, lazy: bool = False, raise_404: bool = False) -> TModel:
        instance = await self.repository.get(item_id, lazy=lazy)
        if instance is None and raise_404:
            raise DoesNotExist()
        return instance

    # async def get_list(self):
    #     return await ''
    #
    # async def create(self):
    #     return await ''
    #
    # async def update(self):
    #     return await ''
    #
    # async def delete(self):
    #     return await ''
