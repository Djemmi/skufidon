from Obstacle.obstacle import Obstacle


class Tree(Obstacle):

    def __init__(self, posX, posY):
        super().__init__("Tree", (posX, posY), {
            "default": "Obstacle/Obstacles/textures/tree_64_76.png",
            "animation_1": "Obstacle/Obstacles/textures/tree_64_76_anim.png"
        }, True, 1)
