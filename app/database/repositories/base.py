import abc


class BaseRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, *args, **kwargs):
        """Получить что-либо по идентификатору"""
        ...
