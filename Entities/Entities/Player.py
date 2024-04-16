import main
from Entities.Entity import Entity


class Player(Entity):

    animation_tick = 0
    # Player size is 14x16 when moving top / botton and 12x14 when moving right / left

    def __init__(self, position: tuple):
        super().__init__("Player", position, {})
        self.locationHandler = main.MainThread.getlocationHandler()

    def moveRelative(self, relativeCoordinates: tuple, obstacles):


        next_x = self.pos_x + relativeCoordinates[0]
        next_y = self.pos_y + relativeCoordinates[1]

        for obstacle in obstacles:
            if obstacle.getX() < next_x < obstacle.getX() + obstacle.getWidth():
                if obstacle.getY() < next_y < obstacle.getY() + obstacle.getHeight():
                    return

        self.pos_x += next_x
        self.pos_y += next_y


