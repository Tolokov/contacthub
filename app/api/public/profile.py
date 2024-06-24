from fastapi import APIRouter

router = APIRouter()


@router.get("/profile", summary="Получение информации о компании", status_code=200)
def get_profile():
    """
    :param: profile_id
    :return: list[instance]
    """
    return NotImplemented


@router.post("/profile", summary="Добавление информации о компании", status_code=200)
def post_profile():
    """
    :param: {
        profile_id: None,
        ...
        models data
        ...
    }
    :return: list[instance]
    """
    return NotImplemented


@router.patch("/profile", summary="Изменение информации о компании", status_code=200)
def patch_profile():
    """
    :param: {
        profile_id: profile_id
        ...
        models data
        ...
        }
    :return: list[id]
    """
    return NotImplemented


@router.delete("/profile", summary="Удаление информации о компании", status_code=200)
def delete_profile():
    """
    :param: profile_id, user_token, 
    :return: 
    """
    return NotImplemented
