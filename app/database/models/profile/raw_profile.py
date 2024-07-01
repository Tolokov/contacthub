from typing import Optional

from sqlalchemy import Text, String
from sqlalchemy.types import JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.database.core.base import BaseModel


class Raw(BaseModel):
    __tablename__ = 'raw_profile'
    __doc__ = """
    Храним сырые данные в базе строкой, со всеми отступами и данными
    для последующего занесения в базу данных и предположительную
    кодировку строки. Данные не безопасны.
    
    Так же если данные хоть как то валидированы лучше хранить джейсонку
    """
    raw_data: Mapped[Optional[str]] = mapped_column(Text)
    parsed_data: Mapped[Optional[JSON]] = mapped_column(type_=JSON, nullable=False)
    coding: Mapped[Optional[str]] = mapped_column(String(20))
