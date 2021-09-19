from truck_delivery_fernando.person import Person


class Driver(Person):
    """Class representing a driver"""

    def __init__(self, ci, name, email, cellphone, age, address, licence_number, licencse_country):
        super(Driver, self).__init__(ci, name, email, cellphone, age)
        self.address = address
        self.license_number = licence_number
        self.license_country = licencse_country

    def show_identification(self):
        return f"Licence: {self.license_number} - Licence Country: {self.license_country} - Name: {self.name}"
