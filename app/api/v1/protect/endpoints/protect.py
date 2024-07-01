
from fastapi import APIRouter

router = APIRouter()


@router.post("/load", summary="Сохранение информации о компаниях в базу из других сервисов", status_code=200)
def post_profiles():
    """Загружаем пакет уже валидированных данных"""
    return NotImplementedError("Метод не реализован")


@router.delete("/load", summary="Удаление информации о компании", status_code=200)
def delete_profiles():
    """Полное удаление данных о компании (тут можно использовать uuid) Полное"""
    return NotImplementedError("Метод не реализован")
