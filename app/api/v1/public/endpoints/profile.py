from fastapi import APIRouter

router = APIRouter()


@router.get("/profile", summary="Получение информации о компании", status_code=200)
def get_profile():
    """Страница компании (все данные о ней)"""
    return NotImplementedError("Метод не реализован")


@router.post("/profile", summary="Добавление информации о компании", status_code=200)
def post_profile():
    """Джейсонка по которой мы создаем страницу компании"""
    return NotImplementedError("Метод не реализован")


@router.patch("/profile", summary="Изменение информации о компании", status_code=200)
def patch_profile():
    """Измменение конкретных пунктов в описании компании"""
    return NotImplementedError("Метод не реализован")


@router.delete("/profile", summary="Удаление информации о компании", status_code=200)
def delete_profile():
    """Удаление записи о компании по идентификатору, со всеми данными о ней (deleted = True)"""
    return NotImplementedError("Метод не реализован")
