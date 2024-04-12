import pygame


class Player:

    def __init__(self, pos_x, pos_y):
        self.player_x = pos_x
        self.player_y = pos_y

    def handleActions(self, pressed_keys, obstacles):
        if pressed_keys[pygame.K_w]:
            self.moveRelative((0, -1), obstacles)
        if pressed_keys[pygame.K_a]:
            self.moveRelative((-1, 0), obstacles)
        if pressed_keys[pygame.K_s]:
            self.moveRelative((0, 1), obstacles)
        if pressed_keys[pygame.K_d]:
            self.moveRelative((1, 0), obstacles)

    def getX(self):
        return self.player_x

    def getY(self):
        return self.player_y

    def setX(self, new_x: int):
        self.player_x = new_x

    def setY(self, new_y: int):
        self.player_y = new_y

    def getPosition(self):
        return self.player_x, self.player_y

    def setPosition(self, pos: tuple):
        self.player_x = pos[0]
        self.player_y = pos[1]

    def moveRelative(self, move: tuple, obstacles) -> tuple:

        # TODO somehow add obstacle check
        # to do that just get next move coords and check location for obstacle at that place
        # or just google what pygame.rect is
        next_x = self.player_x + move[0]
        next_y = self.player_y + move[1]
        for obstacle in obstacles:
            if obstacle.getX() < next_x < obstacle.getX() + obstacle.getWidth():
                if obstacle.getY() < next_y < obstacle.getY() + obstacle.getHeight():
                    return self.player_x, self.player_y

        self.player_x += move[0]
        self.player_y += move[1]

        return self.player_x, self.player_y
