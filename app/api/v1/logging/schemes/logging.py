from typing import Optional

from fastapi import Query
from fastapi_filter.contrib.sqlalchemy.filter import Filter
from pydantic import BaseModel, Field

from app.database.models.logs import LoggerLevel, ClientLevel, Logs


class LogIn(BaseModel):
    """Форма ввода логов"""
    message: str
    log_level: LoggerLevel = LoggerLevel.INFO
    client_level: ClientLevel = ClientLevel.LOCAL


class LogInResponse(BaseModel):
    id: int = Field(description='Идентификатор')


class LogResponse(BaseModel):
    """Валидируемый ответ"""
    id: int = Field(description='Идентификатор лога')
    message: str | None = Field(description='Текст сообщения')
    log_level: str | None = Field(description='Уровень логирования')
    client_level: str | None = Field(description='Уровень автора')


class LogFilter(Filter):
    """Фильтры документации"""

    id: int | None = Field(Query(default=None, description='Идентификатор Лога'))
    log_level: Optional[LoggerLevel] | None = Field(Query(default=None, description='Уровень логирования'))
    client_level: Optional[ClientLevel] | None = Field(Query(default=None, description='Уровень автора'))
    limit: Optional[int] | None = Field(Query(default=25, description='Количество логов'))

    class Constants(Filter.Constants):
        model = Logs
