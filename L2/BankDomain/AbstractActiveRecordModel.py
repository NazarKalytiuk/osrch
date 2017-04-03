from abc import ABCMeta, abstractmethod, abstractproperty
class AbstractARModel:
    __metaclass__ = ABCMeta

    @abstractmethod
    def load(self):
        """Load item"""

    @abstractmethod
    def save(self):
        """зберегти або оновити об'єкт в БД"""

    @abstractmethod
    def _update(self):
        """оновити запис"""

    @abstractmethod
    def delete(self):
        """видалити записи про об'єкт з БД"""
