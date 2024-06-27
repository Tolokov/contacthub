from typing import Optional
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from app.database.core.base import BaseModel

from enum import IntEnum


class LoggerLevel(IntEnum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5


class ClientLevel(IntEnum):
    LOCAL = 1
    PUBLIC = 2


class Logs(BaseModel):
    __tablename__ = 'logs'
    __doc__ = 'Logs table'

    log_level: Mapped[Optional[LoggerLevel]] = mapped_column(default=LoggerLevel.INFO)
    message: Mapped[Optional[str]]
    timestamp: Mapped[Optional[datetime]] = mapped_column(default=datetime.now())
    client_level: Mapped[Optional[ClientLevel]] = mapped_column(default=ClientLevel.LOCAL)
