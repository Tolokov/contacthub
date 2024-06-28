from pydantic import BaseModel
from app.database.models.logs import LoggerLevel, ClientLevel


class LogIn(BaseModel):
    message: str
    log_level: LoggerLevel = LoggerLevel.INFO
    client_level: ClientLevel = ClientLevel.LOCAL
