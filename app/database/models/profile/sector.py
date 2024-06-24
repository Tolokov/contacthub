from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.core.base import BaseModel


class Sector(BaseModel):
    __tablename__ = 'sector'
    __doc__ = """
    Индустрия и область в которой работает компания
    У компании может быть несколько отраслей.
    По идее у компании с одним названием может быть
    производство в разных отраслях, но это не так важно
    """

    profile: Mapped[int] = mapped_column(ForeignKey("profile.id"))
    name: Optional[Mapped[str]]
