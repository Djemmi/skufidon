from Obstacle.Obstacles.Tree import Tree
from Location.Location import Location


class TestLocation(Location):

    def __init__(self):
        self.name = "Test"
        self.texture = "Location/Locations/textures/vasserman.jpg"

        self.obstacles.append(Tree(130, 95))
        self.obstacles.append(Tree(190, 95))

        self.obstacles.append(Tree(100, 100))
        self.obstacles.append(Tree(160, 100))

