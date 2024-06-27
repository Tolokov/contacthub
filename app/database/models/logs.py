from typing import Optional
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from app.database.core.base import BaseModel

from enum import StrEnum


class LoggerLevel(StrEnum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'


class ClientLevel(StrEnum):
    LOCAL = 'LOCAL'
    PUBLIC = 'PUBLIC'


class Logs(BaseModel):
    __tablename__ = 'logs'
    __doc__ = 'Logs table'

    log_level: Mapped[Optional[LoggerLevel]] = mapped_column(default=LoggerLevel.INFO)
    message: Mapped[Optional[str]]
    timestamp: Mapped[Optional[datetime]] = mapped_column(default=datetime.now())
    client_level: Mapped[Optional[ClientLevel]] = mapped_column(default=ClientLevel.LOCAL)
