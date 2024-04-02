import pygame
from Player import Player


class Obstacle:

    def __init__(self, pos: tuple, width: int, height: int, textures: map):
        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.width = width
        self.height = height

        # TODO add empty texture
        self.textures = textures

    def isTouching(self, p: tuple) -> bool:

        touch_x = self.pos_x < p[0] < (self.pos_x + self.width)
        touch_y = self.pos_y < p[1] < (self.pos_y + self.height)

        return touch_x and touch_y

    # getters & setters

    def getRect(self) -> pygame.Rect:
        return pygame.Rect((self.pos_x, self.pos_y), (self.width, self.height))

    def getX(self) -> int:
        return self.pos_x

    def getY(self) -> int:
        return self.pos_x

    def getPos(self) -> tuple:
        return self.pos_x, self.pos_y

    def getHeight(self) -> int:
        return self.height

    def getWidth(self) -> int:
        return self.width

