from Location.Location import Location
from Location.Locations.Limbo import Limbo
from Location.Locations.TestLocation import TestLocation


class locationHandler:

    def __init__(self):
        self.locations: dict = {
            "Limbo": Limbo(),
            "TestLocation": TestLocation()
        }

        self.currentLocation: Location = self.locations.get("TestLocation")

    def getCurrentLocationName(self):
        return self.currentLocation.getName()

    def getCurrentLocation(self) -> Location:
        return self.currentLocation

    def getRightLocation(self):
        if self.currentLocation.getName() == "Limbo":
            return self.locations.get("TestLocation")
        return self.locations.get("Limbo")

    def getLeftLocation(self):
        if self.currentLocation.getName() == "Limbo":
            return self.locations.get("Limbo")
        if self.currentLocation.getName() == "TestLocation":
            return self.locations.get("Limbo")
        return self.locations.get("Limbo")

    def getTopLocation(self):
        if self.currentLocation.getName() == "Limbo":
            return self.locations.get("Limbo")
        if self.currentLocation.getName() == "TestLocation":
            return self.locations.get("Limbo")
        return self.locations.get("Limbo")

    def getBottomLocation(self):
        if self.currentLocation.getName() == "Limbo":
            return self.locations.get("Limbo")
        return self.locations.get("Limbo")

    def getLocationByName(self, name: str) -> Location:
        return self.locations.get(name)

    def setCurrentLocation(self, newLocation: str):
        self.currentLocation = self.locations.get(newLocation)

