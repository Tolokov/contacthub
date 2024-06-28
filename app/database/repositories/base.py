import abc


class BaseRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, *args, **kwargs):
        """Получить что-либо по идентификатору"""
        ...

    # @abc.abstractmethod
    # def create(self, *args, **kwargs):
    #     """Создать новую запись в бд"""
    #     ...
    #
    # @abc.abstractmethod
    # def delete(self, *args, **kwargs):
    #     """Удалить запись из БД"""
    #     ...
