from Location.Location import Location
from Obstacle.Obstacles.Tree2 import Tree2


class Limbo(Location):

    def __init__(self):
        super().__init__()
        self.name = "Limbo"
        self.texture = "Location/Locations/textures/grass2.jpg"

        self.obstacles.append(Tree2(200, 400))
