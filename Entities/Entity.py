import pygame


class Entity():

    def __init__(self, name, positon: tuple, textures: dict):
        self.name = name

        self.pos_x = positon[0]
        self.pos_y = positon[1]

        # Technically, I should use sth between obstacle and entity classes but fuck you I don't care
        if len(textures) < 1:
            print("MISSING DEFAULT TEXTURE OF " + name + " ENTITY")
            self.textures = {"default": "Obstacle/Obstacles/textures/missingTexutre.png"}
        else:
            print("Object texture loaded for " + name)
            self.textures = textures
        self.currentTexture = pygame.image.load(self.textures.get('default'))

    def moveRelative(self, relativeCoordinates: tuple):
        self.pos_x += relativeCoordinates[0]
        self.pos_y += relativeCoordinates[1]
