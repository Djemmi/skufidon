import pygame

from Obstacle.obstacle import Obstacle


class Location:
    obstacles = []
    texture = ""

    def getObstacles(self) -> list[Obstacle]:
        return self.obstacles
