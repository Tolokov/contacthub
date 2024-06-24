from enum import IntEnum

from sqlalchemy.orm import Mapped

from app.database.core.base import BaseModel


class LevelAccess(IntEnum):
    READ = 1
    WRITE = 2
    DELETE = 3


class Token(BaseModel):
    __tablename__ = 'token'
    __doc__ = 'authorization tokens'

    token: Mapped[str]
