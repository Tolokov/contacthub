
from fastapi import APIRouter

router = APIRouter()


@router.post("/load", summary="Сохранение ифнормации о компаниях в базу из других сервисов", status_code=200)
def post_profiles():
    """
    Каждой группе запросов должен выдаваться отдельный uuid с датой загрузки
    чтобы можно было удалить сраазу группу пакетов некорректных данных

    :param: json package {
        SOURCE
    }
    :return:
    """
    return NotImplemented


@router.delete("/load", summary="Удаление информации о компании", status_code=200)
def delete_profiles():
    """
    :param: uuid
    :return:
    """
    return NotImplemented
