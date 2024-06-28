from dataclasses import dataclass

from fastapi import status
from fastapi.exceptions import HTTPException


@dataclass
class DoesNotExist(HTTPException, Exception):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Нет записи с таким id'
