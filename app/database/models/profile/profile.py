import uuid
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.types import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger
from app.database.core.base import BaseModel


class Profile(BaseModel):
    __tablename__ = 'profile'
    __doc__ = """
    Информация о компании, Название может быть одинаковым,
    поэтому можно написать скрипт который будет определять
    совпадающую инфорацию по названию и контактной информации
    и группировать в общую карточку, но лучше пока оставить
    
    Эту информацию мы будем выводить на главной
    """
    title: Mapped[str] = mapped_column(BigInteger, autoincrement=True, primary_key=True)
    tag: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)
    contact: Mapped[list["Contact"]] = relationship(back_populates="profile", cascade="all, delete-orphan")
    # texts: Mapped[list["TextProfile"]] = relationship(back_populates="text_profile", cascade="all, delete-orphan")
    # sectors: Mapped[list["Sector"]] = relationship(back_populates="sector", cascade="all, delete-orphan")


class Contact(BaseModel):
    __tablename__ = 'contact'
    __doc__ = """
    Информация ради которой все затевается, можно продать,
    будет обновляться максимально часто и по ней будет
    осуществляться поиск со строны фронта. Часто будет
    храить сырые, не типизированные данные строкой
    """

    profile_id: Mapped[int] = mapped_column(ForeignKey("profile.id"))
    profile: Mapped["Profile"] = relationship(back_populates="contact")
    # profile: Mapped[int] = mapped_column(ForeignKey("profile.id"), ondelete="CASCADE")

    inn: Mapped[Optional[str]]
    orgn: Mapped[Optional[str]]

    city: Mapped[Optional[str]]
    address: Mapped[Optional[str]]

    phone: Mapped[Optional[str]]
    contact_name: Mapped[Optional[str]]
    contact: Mapped[Optional[str]]


# class TextProfile(BaseModel):
#     __tablename__ = 'text_profile'
#     __doc__ = """
#     Дополнительная информация о компании, очень
#     не структурированная и обычно может содежать
#     в себе излишний текст на разных языках
#     """
#
#     profile_id: Mapped[int] = mapped_column(ForeignKey("profile.id"))
#     profile: Mapped["Profile"] = relationship(back_populates="profile")
#     # profile: Mapped[int] = mapped_column(ForeignKey("profile.id"), ondelete="CASCADE")
#
#     description: Mapped[Optional[str]]
#     full_address: Mapped[Optional[str]]
#     full_title: Mapped[Optional[str]]
#
#     zip: Mapped[Optional[str]]
#     head: Mapped[Optional[str]]
#
#
# class Sector(BaseModel):
#     __tablename__ = 'sector'
#     __doc__ = """
#     Индустрия и область в которой работает компания
#     У компании может быть несколько отраслей.
#     По идее у компании с одним названием может быть
#     производство в разных отраслях, но это не так важно
#     """
#
#     profile_id: Mapped[int] = mapped_column(ForeignKey("profile.id"))
#     profile: Mapped["Profile"] = relationship(back_populates="profile")
#     name: Mapped[Optional[str]]


# class Addition(BaseModel):
#     __tablename__ = 'addition'
#     __doc__ = 'Addition table if other table need more datas'
#
#     data: Mapped[JSON] = mapped_column(type_=JSON, nullable=False)
