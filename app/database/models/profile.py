from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.core.base import BaseModel


class Profile(BaseModel):
    __tablename__ = 'profile'
    __doc__ = 'The most important model, most dubl and dinamics'

    title: str = mapped_column()


class ContactProfile(BaseModel):
    __tablename__ = 'contact_profile'
    __doc__ = 'Contact information'

    profile: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    inn: str
    orgn: str
    city: str
    state: str
    zip: str
    address: str
    phone: str


class TextProfile(BaseModel):
    __tablename__ = 'text'
    __doc__ = 'Not important model'

    profile: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    description: str
    full_address: str
    full_title: str













