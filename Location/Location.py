import pygame

from Obstacle.obstacle import Obstacle


class Location:
    def __init__(self):
        self.name = ""
        self.obstacles = []
        self.texture = ""

    def getObstacles(self) -> list[Obstacle]:
        # print(f"Returning obstacles for location {self.name} here they are: {self.obstacles}")
        return self.obstacles

    def getName(self):
        return self.name
