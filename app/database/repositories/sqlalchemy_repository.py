from app.database.core.base import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.repositories.base import BaseRepository

TModel = TypeVar('TModel', bound=BaseModel)


class SqlalchemyRepository(BaseRepository, Generic[TModel]):
    model: type[TModel]

    def __init__(self, session: AsyncSession):
        self.session = session

    # async def get(self, *args, **kwargs):
    #     """Получить что-либо по идентификатору"""
    #     return await ''

    async def get(self, item_id: int, lazy: bool = False) -> TModel:
        query = self._get_select_query(lazy).filter(getattr(self.model, 'id') == item_id)

        instance = await self.session.scalar(query)

        return instance

    async def create(self, *args, **kwargs):
        """Создать новую запись в бд"""
        return await ''

    async def delete(self, *args, **kwargs):
        """Удалить запсись из БД"""
        return await ''


    # def __init__(self, session: AsyncSession):
    #     self.session = session
    #
    # def _get_select_query(self, lazy: bool = True) -> Select:
    #     query = select(self.model).order_by(getattr(self.model, 'id'))
    #     if hasattr(self.model, 'deleted'):
    #         query = query.filter(getattr(self.model, 'deleted') == false())
    #     if lazy:
    #         query = query.options(raiseload('*'))
    #     return query
    #
    # async def get_list(self, filters: Filter = None, lazy: bool = True, query: Select = None, **kwargs) -> list[TModel]:
    #     query = query if query is not None else self._get_select_query(lazy).filter_by(**kwargs)
    #
    #     if filters is not None:
    #         query = filters.filter(query)
    #         query = filters.sort(query)
    #
    #     result = await self.session.execute(query)
    #     return list(result.unique().scalars().all())
    #
    # async def get(self, item_id: int, lazy: bool = False) -> TModel:
    #     query = self._get_select_query(lazy).filter(getattr(self.model, 'id') == item_id)
    #
    #     instance = await self.session.scalar(query)
    #
    #     return instance
    #
    # async def create(self, instance: TModel) -> TModel:
    #     self.session.add(instance)
    #     await self.session.flush()
    #     await self.session.refresh(instance)
    #     return instance
    #
    # async def create_list(self, instances: list[TModel]) -> list[TModel]:
    #     self.session.add_all(instances)
    #     await self.session.flush()
    #     for instance in instances:
    #         await self.session.refresh(instance)
    #     return instances
    #
    # async def update(self, instance: TModel) -> TModel:
    #     await self.session.flush()
    #     await self.session.refresh(instance)
    #     return instance
    #
    # async def update_list(self, instances: list[TModel]) -> list[TModel]:
    #     await self.session.flush(instances)
    #     for instance in instances:
    #         await self.session.refresh(instance)
    #     return instances
    #
    # async def delete(self, instance: TModel):
    #     await self.session.delete(instance)
    #     await self.session.flush()
    #
    # async def delete_list(self, instances: list[TModel]) -> None:
    #     for instance in instances:
    #         await self.session.delete(instance)
    #     await self.session.flush()


class ModelRepository(SqlalchemyRepository, Generic[TModel]):
    def __init__(self, session: AsyncSession, model: type[TModel]):
        self.model = model
        super().__init__(session)
