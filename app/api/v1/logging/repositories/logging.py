from app.database.repositories.sqlalchemy_repository import SqlalchemyRepository
from app.database.models.logs import Logs


class LogsRepository(SqlalchemyRepository):
    model = Logs
