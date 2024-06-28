from sqlalchemy.ext.asyncio import AsyncSession

from app.database.core.engine import session
from app.database.models.logs import Logs
from app.database.services.sqlalchemy_service import SqlalchemyService

from app.lib.exceptions import DoesNotExist
from app.api.v1.logging.repositories.logging import LogsRepository


class LogService(SqlalchemyService[Logs]):
    model = Logs

    def __init__(self, session: AsyncSession):
        self.repository = LogsRepository(session)

    async def get(
            self, item_id: int, lazy: bool = False, raise_404: bool = False
    ) -> Logs | None:
        instance = await self.repository.get(item_id, lazy=lazy)
        if instance is None and raise_404:
            raise DoesNotExist()
        return instance
