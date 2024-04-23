from Location.Location import Location
from Obstacle.Obstacles.Tree2 import Tree2


class Limbo(Location):

    def __init__(self):
        super().__init__()
        self.name = "Limbo"
        self.texture = "Location/Locations/textures/proof1.png"

        self.obstacles.append(Tree2(200, 400))
