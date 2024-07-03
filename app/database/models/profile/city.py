from sqlalchemy import ForeignKey

from app.database.core.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship


class District(BaseModel):
    __tablename__ = 'district'
    __doc__ = """Регионы"""

    contact: Mapped[list["City"]] = relationship(back_populates="profile", cascade="save-update")
    district_number: Mapped[int]
    district_name: Mapped[str]


class City(BaseModel):
    __tablename__ = 'city'
    __doc__ = """Города"""

    city_name: Mapped[str]
    district_id: Mapped[int] = mapped_column(ForeignKey('district.id'), primary_key=True)
