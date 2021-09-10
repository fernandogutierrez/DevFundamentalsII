from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    """Class to define basic information of a person"""

    def __init__(self, ci, name, email, cellphone, age):
        self.name = name
        self.ci = ci
        self.email = email
        self.cellphone = cellphone
        self.age = age

    @abstractmethod
    def __to_dict(self):
        """something -> This method need to be implemented"""
