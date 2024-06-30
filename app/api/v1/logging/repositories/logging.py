from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy import select

from app.database.models.logs import Logs
from app.database.repositories.sqlalchemy_repository import SqlalchemyRepository


class LogsRepository(SqlalchemyRepository):
    model = Logs

    async def get(self, filters: Filter = None, limit: int = 10, lazy: bool = False) -> list[Logs]:
        query = select(self.model).order_by(self.model.id.desc()).limit(limit)

        if filters is not None:
            query = filters.filter(query)

        result = await self.session.execute(query)
        return list(result.scalars().all())
