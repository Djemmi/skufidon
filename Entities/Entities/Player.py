import pygame.image

from Entities.Entity import Entity


class Player(Entity):
    animation_tick = 0
    # Player size is 14x16 when moving top / botton and 12x14 when moving right / left

    right = {
        "right1": "Entities/Entities/textures/player_right/right_1.png",
        "right2": "Entities/Entities/textures/player_right/right_2.png",
        "right3": "Entities/Entities/textures/player_right/right_3.png",
        "right4": "Entities/Entities/textures/player_right/right_4.png"
    }
    left = {
        "left1": "Entities/Entities/textures/player_left/left_1.png",
        "left2": "Entities/Entities/textures/player_left/left_2.png",
        "left3": "Entities/Entities/textures/player_left/left_3.png",
        "left4": "Entities/Entities/textures/player_left/left_4.png"
    }
    top = {
        "top1": "Entities/Entities/textures/player_top/top_1.png",
        "top2": "Entities/Entities/textures/player_top/top_2.png",
        "top3": "Entities/Entities/textures/player_top/top_3.png",
        "top4": "Entities/Entities/textures/player_top/top_4.png"
    }
    bottom = {
        "bottom1": "Entities/Entities/textures/player_bottom/bottom_1.png",
        "bottom2": "Entities/Entities/textures/player_bottom/bottom_2.png",
        "bottom3": "Entities/Entities/textures/player_bottom/bottom_3.png",
        "bottom4": "Entities/Entities/textures/player_bottom/bottom_4.png",
    }

    def __init__(self, position: tuple):
        super().__init__("Player", position, {})
        self.width = 16
        self.height = 16
        self.currentTexture = pygame.transform.scale(pygame.image.load(self.bottom.get("bottom1")), (28, 32))


    def moveRelative(self, relativeCoordinates: tuple, obstacles):
        next_x = self.pos_x + relativeCoordinates[0]
        next_y = self.pos_y + relativeCoordinates[1]

        self.pos_x += next_x
        self.pos_y += next_y

    def getCurrentTexture(self):
        return self.currentTexture

