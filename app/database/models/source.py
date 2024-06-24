from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from app.database.core.base import BaseModel


class Source(BaseModel):
    __tablename__ = 'source'
    __doc__ = 'Описание сайте, с которого взята информация о компании, для статистики'

    name: Optional[Mapped[str]]
    link: Optional[Mapped[str]]
    icon: Optional[Mapped[str]]
    format_icon: Optional[Mapped[str]]
    description: Optional[Mapped[str]]

    date_update: Mapped[datetime] = mapped_column(comment="Date of update", default=datetime.now())
    date_created: Mapped[datetime] = mapped_column(comment="Date of created", default=datetime.now())

    user_auth: Optional[Mapped[str]]
    user_login: Optional[Mapped[str]]
    user_data: Optional[Mapped[str]]