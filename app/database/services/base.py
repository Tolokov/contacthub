import abc


class BaseService(abc.ABC):
    @abc.abstractmethod
    def get(self,  *args, **kwargs):
        """Получить что-либо по идентификатору. Только чтение"""
        ...

    # @abc.abstractmethod
    # def get_list(self,  *args, **kwargs):
    #     """Получить список записей. Только чтение"""
    #     ...
    #
    # @abc.abstractmethod
    # def create(self,  *args, **kwargs):
    #     """Создать новую запись в бд"""
    #     ...
    #
    # @abc.abstractmethod
    # def update(self,  *args, **kwargs):
    #     """Обновить запись в БД"""
    #     ...
    #
    # @abc.abstractmethod
    # def delete(self,  *args, **kwargs):
    #     """Удалить запись из БД"""
    #     ...
