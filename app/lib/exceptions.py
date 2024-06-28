import dataclasses

from fastapi import status
from fastapi.exceptions import HTTPException


@dataclasses.dataclass
class DoesNotExist(HTTPException, Exception):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Нет записи с таким id'
