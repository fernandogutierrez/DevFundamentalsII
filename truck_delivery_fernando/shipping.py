class Shipping:
    """Facade Shipping Class"""
    def __init__(self, truck, driver, client, start_place, end_place, packages, status, identifier):
        self.truck = truck
        self.driver = driver
        self.client = client
        self.start_place = start_place
        self.end_place = end_place
        self.packages = packages
        self.status = status
        self.identifier = identifier

    def get_current_truck_location(self):
        """
        get_current_location --> getting the current location GPS coordinates.
        Return:
             result(String)
        """
        return self.truck.get_location()

    def get_truck_humidity_level(self):
        """
        get_truck_humidity_level --> getting the current humidity level in percentage units of a truck
        Return:
             result(String)
        """
        return self.truck.get_humidity_level()

    def get_truck_temperature_level(self):
        """
        get_truck_temperature_level --> getting the current temperature level in percentage units of a truck
        Return:
             result(String)
        """
        return self.truck.get_temperature_level()

