import uuid
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.core.base import BaseModel


class Profile(BaseModel):
    __tablename__ = 'profile'
    __doc__ = """
    Информация о компании, Название может быть одинаковым,
    поэтому можно написать скрипт который будет определять
    совпадающую инфорацию по названию и контактной информации
    и группировать в общую карточку, но лучше пока оставить
    """

    title: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column(default_factory=uuid.uuid4)


class ContactProfile(BaseModel):
    __tablename__ = 'contact_profile'
    __doc__ = """
    Информация ради которой все затевается, можно продать,
    будет обновляться максимально часто и по ней будет 
    осуществляться поиск со строны фронта. Часто будет 
    храить сырые, не типизированные данные строкой
    """

    profile: Mapped[int] = mapped_column(ForeignKey("profile.id"), ondelete="CASCADE")

    inn: Optional[Mapped[str]]
    orgn: Optional[Mapped[str]]

    city: Optional[Mapped[str]]
    address: Optional[Mapped[str]]

    phone: Optional[Mapped[str]]
    contact_name: Optional[Mapped[str]]
    contact: Optional[Mapped[str]]


class TextProfile(BaseModel):
    __tablename__ = 'text_profile'
    __doc__ = """
    Дополнительная информация о компании, очень 
    не структурированная и обычно может содежать
    в себе излишний текст на разных языках
    """

    profile: Mapped[int] = mapped_column(ForeignKey("profile.id"), ondelete="CASCADE")
    description: Optional[Mapped[str]]
    full_address: Optional[Mapped[str]]
    full_title: Optional[Mapped[str]]
    zip: Optional[Mapped[str]]
    head: Optional[Mapped[str]]
