from fastapi import APIRouter

router = APIRouter()


@router.get("/profiles", summary="Получение информации о компании", status_code=200)
def get_profiles():
    """
    :param: limit, page, profile_id, others...
    :return: list[instance]
    """
    return NotImplemented


@router.post("/profiles", summary="Добавление информации о компании", status_code=200)
def post_profiles():
    """
    :param: json package {
        profile_id: None,
        ...
        models data
        ...
    }
    :return: list[instance]
    """
    return NotImplemented


@router.patch("/profiles", summary="Изменение информации о компании", status_code=200)
def patch_profiles():
    """
    :param: json package {
        profile_id: profile_id {
            ...
            models data
            ...}
        }
    :return: list[id]
    """
    return NotImplemented


@router.delete("/profiles", summary="Удаление информации о компании", status_code=200)
def delete_profiles():
    """
    :param: list[profile_id]}
    :return:
    """
    return NotImplemented
