import pygame


class Entity:
    def __init__(self, name, positon: tuple, textures: dict):
        self.name = name

        self.pos_x = positon[0]
        self.pos_y = positon[1]
        self.width = 0
        self.height = 0

        # Technically, I should use sth between obstacle and entity classes but fuck you I don't care
        if len(textures) < 1:
            print("MISSING DEFAULT TEXTURE OF " + name + " ENTITY")
            self.textures = {"default": "Obstacle/Obstacles/textures/missingTexutre.png"}
        else:
            print("Object texture loaded for " + name)
            self.textures = textures
        self.currentTexture = pygame.image.load(self.textures.get('default'))

    def moveRelative(self, relativeCoordinates: tuple, obstacles):

        next_x = self.pos_x + relativeCoordinates[0]
        next_y = self.pos_y + relativeCoordinates[1]

        for obstacle in obstacles:
            if obstacle.getX() < next_x < obstacle.getX() + obstacle.getWidth() or obstacle.getX() < next_x + self.getWidth() < obstacle.getX() + obstacle.getWidth():
                if obstacle.getY() < next_y < obstacle.getY() + obstacle.getHeight() or obstacle.getY() < next_y + self.getHeight() < obstacle.getY() + obstacle.getHeight():
                    return
            # TODO tryna add check if obstacle side is smaller than player's so player wont move throw it
            # мне пизедец как лень это фиксить, как будет больше пива может быть
            # if self.getWidth() > obstacle.getWidth() or self.getHeight() < obstacle.getHeight():
            #     return
            # if obstacle.getY() > self.getY() or obstacle.getY() + obstacle.getHeight() < self.getY() + self.getHeight() and obstacle.getX() > self.getX() or obstacle.getX() + obstacle.getWidth() < self.getX() + self.getWidth():
            #     return

        self.pos_x = next_x
        self.pos_y = next_y


    def getX(self):
        return self.pos_x

    def getY(self):
        return self.pos_y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height