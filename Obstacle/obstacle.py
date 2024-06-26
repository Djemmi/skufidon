import random

import pygame
from pygame import Surface, SurfaceType


class Obstacle:
    def __init__(self, name: str, pos: tuple, textures: dict, isAnimated=False, animationLastFrame=0):
        # TODO probably add field like "passable" to make possible to create intangible objects
        self.name = name
        self.isAnimated = isAnimated
        self.animationTick = 60 + random.randint(0, 20)
        # Shitty thing, means number of animation texture number curr playing
        self.animationFrame = 0
        # TODO make it as constructor parameter
        self.animationLastFrame = animationLastFrame

        self.pos_x = pos[0]
        self.pos_y = pos[1]

        if len(textures) < 1:
            print("MISSING TEXTURE OF " + name + " OBJECT")
            self.textures = {"default": "Obstacle/Obstacles/textures/missingTexutre.png"}
        else:
            print("Object texture loaded for " + name)
            self.textures = textures
        self.currentTexture = pygame.image.load(self.textures.get('default'))

        self.width = self.currentTexture.get_width()
        self.height = self.currentTexture.get_height()

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

    def getX(self):
        return self.pos_x

    def getY(self):
        return self.pos_y

    def getPos(self) -> tuple:
        return self.getX(), self.getY()

    def getHeight(self):
        return self.height

    def getWidth(self):
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

    def hasAnimation(self):
        return self.isAnimated
