from abc import ABCMeta, abstractmethod, ABC


class ContentManager:
    def __init__(self):
        pass

    @abstractmethod
    def save_document(self, object):
        pass

    @abstractmethod
    def get_document(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self, object_id):
        pass
