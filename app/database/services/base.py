import abc


class BaseService(abc.ABC):
    @abc.abstractmethod
    def get(self,  *args, **kwargs):
        """Получить что-либо по идентификатору. Только чтение"""
        ...
