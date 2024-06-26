from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from app.database.core.base import BaseModel


class Resource(BaseModel):
    __tablename__ = 'resource'
    __doc__ = 'Описание сайте, с которого взята информация о компании, для статистики'

    name: Mapped[Optional[str]]
    link: Mapped[Optional[str]]
    icon: Mapped[Optional[str]]
    format_icon: Mapped[Optional[str]]
    description: Mapped[Optional[str]]

    date_update: Mapped[datetime] = mapped_column(comment="Date of update", default=datetime.now())
    date_created: Mapped[datetime] = mapped_column(comment="Date of created", default=datetime.now())

    user_auth: Mapped[Optional[str]]
    user_login: Mapped[Optional[str]]
    user_data: Mapped[Optional[str]]
