from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.logs import Logs
from app.database.services.sqlalchemy_service import SqlalchemyService
from app.api.v1.logging.repositories.logging import LogsRepository


class LogService(SqlalchemyService[Logs]):
    model = Logs

    def __init__(self, session: AsyncSession):
        self.repository = LogsRepository(session)

    async def get(
            self,
            filters: Filter = None,
            lazy: bool = False,
            raise_404: bool = False
    ) -> list[Logs]:

        limit = getattr(filters, "limit")
        delattr(filters, "limit")

        instance = await self.repository.get(filters, limit, lazy=lazy)
        return instance
