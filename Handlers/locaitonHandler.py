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

    def getRightLocation(self, currentLocation: Location):
        if isinstance(currentLocation, Limbo):
            return self.Limbo

    def getLeftLocation(self, currentLocation: Location):
        if isinstance(currentLocation, Limbo):
            return self.Limbo

    def getTopLocation(self, currentLocation: Location):
        if isinstance(currentLocation, Limbo):
            return self.Limbo
        if isinstance(currentLocation, TestLocation):
            return self.Limbo

    def getBottomLocation(self, currentLocation: Location):
        if isinstance(currentLocation, Limbo):
            return self.Limbo

