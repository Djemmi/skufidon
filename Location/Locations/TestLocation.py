from Obstacle.Obstacles.Tree import Tree
from Location.Location import Location


class TestLocation(Location):

    def __init__(self):
        self.texture = "Location/Locations/textures/fixed_workjpg.jpg"

        self.obstacles.append(Tree(130, 95))
        self.obstacles.append(Tree(190, 95))

        self.obstacles.append(Tree(100, 100))
        self.obstacles.append(Tree(160, 100))


        print("Test location inited")

