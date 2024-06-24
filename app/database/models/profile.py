from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.core.base import BaseModel


class Profile(BaseModel):
    __tablename__ = 'profile'
    __doc__ = 'The most important model, most dubl and dinamics'

    title: str = mapped_column()


class ContactProfile(BaseModel):
    __tablename__ = 'contact_profile'
    __doc__ = 'Contact information for search and filter'

    profile: Mapped[int] = mapped_column(ForeignKey("profile.id"))
    inn: str
    orgn: str
    city: str
    state: str
    zip: str
    address: str
    phone: str
    date_update: datetime = mapped_column(comment="Date of creation")


class TextProfile(BaseModel):
    __tablename__ = 'text_profile'
    __doc__ = 'Not important model, maby lazy load'

    profile: Mapped[int] = mapped_column(ForeignKey("profile.id"))
    description: str
    full_address: str
    full_title: str
    date_created: datetime = mapped_column(comment="Date of creation")














