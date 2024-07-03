from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class BaseModel(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
