from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class BaseModel(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)

    # Функция которая проходит по атрибутам таблицы и заполняет рандомными даннными

    # async def fill_random_data(self):
    #     print('=====')
    #     for i in self.__name__.__dict__.items():
    #         print(i)
    #     # print(self.metadata)
    #     # print(self.id)
    #     print('=====')
    #     return None
