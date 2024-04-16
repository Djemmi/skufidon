import pygame

from Obstacle.obstacle import Obstacle


class Location:
    name = ""
    obstacles = []
    texture = ""

    def getObstacles(self) -> list[Obstacle]:
        return self.obstacles

    def getName(self):
        return self.name

    def getRightLocation(self):
        return "Limbo"

    def getLeftLocation(self):
        return "Limbo"

    def getTopLocation(self):
        return "Limbo"

    def getBottomLocation(self):
        return "Limbo"

    # TODO в пизду, надо делать локешн менеджер
