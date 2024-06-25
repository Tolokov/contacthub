from sqlalchemy.types import JSON
from app.database.core.base import BaseModel
from typing import Any, Optional
from sqlalchemy.orm import Mapped, mapped_column


class Addition(BaseModel):
    __tablename__ = 'addition'
    __doc__ = 'Addition table if other table need more datas'

    data: Mapped[JSON] = mapped_column(type_=JSON, nullable=False)
