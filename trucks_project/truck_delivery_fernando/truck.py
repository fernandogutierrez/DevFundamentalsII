from truck_delivery_fernando.vehicle import Vehicle


class Truck(Vehicle):
    """"Class to define the information of Trucks"""
    def __init__(self, type, name, color, plate, model, brand):
        super(Truck, self).__init__(type, name, color)
        self.plate = plate
        self.model = model
        self.brand = brand
        self.location = "N40° 44.9064', W073° 59.0735'"
        self.humidity_level = "15%"
        self.temperature_level = "20%"

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def get_humidity_level(self):
        return self.humidity_level

    def get_temperature_level(self):
        return self.temperature_level

