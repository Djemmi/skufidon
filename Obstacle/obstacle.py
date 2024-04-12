import random

import pygame
from pygame import Surface, SurfaceType


class Obstacle:
    def __init__(self, name: str, pos: tuple, width: int, height: int, textures: dict, isAnimated=False):
        # TODO probably add field like "passable" to make possible to create intangible objects
        self.name = name
        self.isAnimated = isAnimated
        self.animationTick = 60 + random.randint(0, 20)
        # Shitty thing, means number of animation texture number curr playing
        self.animationFrame = 0
        # TODO make it as constructor parameter
        self.animationLastFrame = 1

        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.width = width
        self.height = height

        if len(textures) < 1:
            print("MISSING TEXTURE OF " + name + " OBJECT")
            self.textures = {"default": "Obstacle/Obstacles/textures/missingTexutre.png"}
        else:
            print("Object texture loaded for " + name)
            self.textures = textures
        self.currentTexture = pygame.image.load(self.textures.get('default'))

    def playAnimation(self):
        if not self.isAnimated:
            return
        self.animationTick -= 1

        if self.animationTick == 0:
            self.animationTick = 60 + random.randint(0, 20)
            if self.animationFrame == self.animationLastFrame:
                self.animationFrame = 0
                self.currentTexture = pygame.image.load(self.textures.get('default'))
            else:
                self.animationFrame += 1
                self.currentTexture = pygame.image.load(self.textures.get('animation_' + str(self.animationFrame)))



    # getters & setters

    def getRect(self) -> pygame.Rect:
        return pygame.Rect((self.pos_x, self.pos_y), (self.width, self.height))

    def getX(self) -> int:
        return self.pos_x

    def getY(self) -> int:
        return self.pos_y

    def getPos(self) -> tuple:
        return self.pos_x, self.pos_y

    def getHeight(self) -> int:
        return self.height

    def getWidth(self) -> int:
        return self.width

    def getName(self):
        return self.name

    # returns ABSOLUTELY useless array of textures, use getCurrentTexture instead
    def getTextures(self):
        return self.textures

    def getCurrentTexture(self) -> None | Surface | SurfaceType:
        if self.currentTexture is None:
            return None
        return self.currentTexture

    def isAnimated(self):
        return self.isAnimated
