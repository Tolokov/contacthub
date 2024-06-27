from enum import IntEnum
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from app.database.core.base import BaseModel


class LevelAccess(IntEnum):
    READ = 1
    WRITE = 2
    DELETE = 3


class Token(BaseModel):
    __tablename__ = 'token'
    __doc__ = 'authorization tokens'

    log_level: Mapped[Optional[LevelAccess]] = mapped_column(default=LevelAccess.READ)
    token: Mapped[str]
    expired: Mapped[bool] = mapped_column(default=False)
