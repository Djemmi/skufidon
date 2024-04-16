from Location.Location import Location
from Location.Locations.Limbo import Limbo
from Location.Locations.TestLocation import TestLocation


class locationHandler:

    def __init__(self):
        self.Limbo = Limbo()
        self.Testlocaton = TestLocation()

        self.currentLocation = self.Limbo

    def getCurrentLocation(self):
        return self.currentLocation
