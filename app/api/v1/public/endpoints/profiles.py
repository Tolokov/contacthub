from fastapi import APIRouter

router = APIRouter()


@router.get("/profiles", summary="Получение информации о компании", status_code=200)
def get_profiles():
    """Список компаний удовлетворяющих условиям"""
    return NotImplementedError("Метод не реализован")


@router.post("/profiles", summary="Добавление информации о компании", status_code=200)
def post_profiles():
    """Добавление списка компаний"""
    return NotImplementedError("Метод не реализован")


@router.patch("/profiles", summary="Изменение информации о компании", status_code=200)
def patch_profiles():
    """Обновление данных о компании согласно списка"""
    return NotImplementedError("Метод не реализован")


@router.delete("/profiles", summary="Удаление информации о компании", status_code=200)
def delete_profiles():
    """Удаление списка компании (Делаеем их скрытыми)"""
    return NotImplementedError("Метод не реализован")
