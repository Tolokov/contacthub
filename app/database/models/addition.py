from app.database.core.base import BaseModel

from sqlalchemy.orm import Mapped
from sqlalchemy.dialects.postgresql import json


class Addition(BaseModel):
    __tablename__ = 'addition'
    __doc__ = 'Addition table if other table need more datas'

    data: Mapped[json]
