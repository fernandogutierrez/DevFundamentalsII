from abc import ABCMeta, abstractmethod


class DBConnector(metaclass=ABCMeta):
    def __init__(self):
        """"""

    @abstractmethod
    def get_connection(self):
        """"""

    @abstractmethod
    def save(self, id_save, object_to_save):
        """"""

    @abstractmethod
    def get_by_id(self, id):
        """"""

    @abstractmethod
    def get_all(self):
        """"""

    @abstractmethod
    def delete(self, id):
        """"""
