from sqlalchemy import ForeignKey

from app.database.core.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship


class District(BaseModel):
    __tablename__ = 'district'
    __doc__ = """Регионы"""

    number: Mapped[int]
    name: Mapped[str]
    city: Mapped[list["City"]] = relationship(back_populates="district", cascade="save-update")


class City(BaseModel):
    __tablename__ = 'city'
    __doc__ = """Города"""

    city_name: Mapped[str]
    district_id: Mapped[int] = mapped_column(ForeignKey('district.id'), primary_key=True)
    district: Mapped["District"] = relationship(back_populates="city")
