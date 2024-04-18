import pygame.image
from Entities.Entity import Entity


class Player(Entity):
    # Player size is 14x16 when moving top / botton and 12x14 when moving right / left

    right = {
        1: "Entities/Entities/textures/player_right/right_1.png",
        2: "Entities/Entities/textures/player_right/right_2.png",
        3: "Entities/Entities/textures/player_right/right_3.png",
        4: "Entities/Entities/textures/player_right/right_4.png"
    }
    left = {
        1: "Entities/Entities/textures/player_left/left_1.png",
        2: "Entities/Entities/textures/player_left/left_2.png",
        3: "Entities/Entities/textures/player_left/left_3.png",
        4: "Entities/Entities/textures/player_left/left_4.png"
    }
    top = {
        1: "Entities/Entities/textures/player_top/top_1.png",
        2: "Entities/Entities/textures/player_top/top_2.png",
        3: "Entities/Entities/textures/player_top/top_3.png",
        4: "Entities/Entities/textures/player_top/top_4.png"
    }
    bottom = {
        1: "Entities/Entities/textures/player_bottom/bottom_1.png",
        2: "Entities/Entities/textures/player_bottom/bottom_2.png",
        3: "Entities/Entities/textures/player_bottom/bottom_3.png",
        4: "Entities/Entities/textures/player_bottom/bottom_4.png",
    }

    def __init__(self, position: tuple):
        super().__init__("Player", position, {})
        self.animation_tick = 1
        self.animation_cooldown = 8
        self.width = 14
        self.height = 16
        # self.locationHandler = main.locationHandler
        self.currentTexture = pygame.transform.scale(pygame.image.load(self.bottom.get(1)), (28, 32))

    def getCurrentTexture(self):
        return pygame.transform.scale(self.currentTexture, (28, 32))
        # return self.currentTexture

    # TODO improve storing of textures and how it changes
    def handleActions(self, pressed_keys, obstacles, screenSize):
        # print(f"player x: {self.pos_x}  y:{self.pos_y}")
        self.animation_cooldown -= 1
        if self.animation_cooldown == 0:
            self.animation_cooldown = 8
            self.animation_tick += 1

        if self.animation_tick > 4:
            self.animation_tick = 1

        if pressed_keys[pygame.K_w]:
            self.currentTexture = pygame.image.load(self.top.get(self.animation_tick))
            self.moveRelative((0, -1), obstacles)
        if pressed_keys[pygame.K_a]:
            self.currentTexture = pygame.image.load(self.left.get(self.animation_tick))
            self.moveRelative((-1, 0), obstacles)
        if pressed_keys[pygame.K_s]:
            self.currentTexture = pygame.image.load(self.bottom.get(self.animation_tick))
            self.moveRelative((0, 1), obstacles)
        if pressed_keys[pygame.K_d]:
            self.currentTexture = pygame.image.load(self.right.get(self.animation_tick))
            self.moveRelative((1, 0), obstacles)

        if self.pos_x < 0:
            print("reached LEFT end")
            # self.locationHandler.getLeftLocation(self.locationHandler.getCurrentLocation())
            self.pos_x = screenSize[0] - self.width * 2
        if self.pos_x + self.width * 2 > screenSize[0]:  # REDO
            print("reached RIGHT end")
            self.pos_x = 0
        if self.pos_y < 0:
            print("reached TOP end")
            self.pos_y = screenSize[1] - self.height * 2
        if self.pos_y + self.height * 2 > screenSize[1]:  # REDO
            print("reached BOTTOM end")
            self.pos_y = 0
