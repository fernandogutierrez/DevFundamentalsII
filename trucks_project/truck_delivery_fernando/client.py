from truck_delivery_fernando.person import Person


class Client(Person):
    """Class representing a client"""
    def __init__(self, ci, name, email, cellphone, age, address, nit):
        print(ci, name, email, cellphone, age, address, nit)
        super(Client, self).__init__(ci, name, email, cellphone, age)
        self.nit = nit
        self.address = address

    def _to_dict(self):
        return self.__dict__

    def show_identification(self):
        return f"Name: {self.name} - CI:{self.ci} - Email {self.email}"
