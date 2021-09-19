from abc import ABCMeta, abstractmethod, ABC


class ContentManager(metaclass=ABC):
    def __init__(self):
        pass

    @abstractmethod
    def save_document(self):
        pass

    @abstractmethod
    def get_document(self):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self):
        pass
