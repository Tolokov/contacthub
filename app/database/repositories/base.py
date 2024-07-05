import abc


class BaseRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, *args, **kwargs):
        """Получить что-либо по идентификатору или фильтру"""
        ...

    @abc.abstractmethod
    def post(self, *args, **kwargs):
        """Положить что-то и получить идентификатор созданной записи"""
