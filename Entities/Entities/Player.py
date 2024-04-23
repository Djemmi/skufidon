import pygame.image
from Entities.Entity import Entity
from Handlers.locaitonHandler import locationHandler


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
        self.width = 14 * 2
        self.height = 16 * 2
        self.locationHandler = locationHandler()
        self.currentTexture = pygame.transform.scale(pygame.image.load(self.bottom.get(1)), (28, 32))

    def getCurrentTexture(self):
        return pygame.transform.scale(self.currentTexture, (28, 32))
        # return self.currentTexture

    # TODO improve storing of textures and how it changes
    def handleActions(self, pressed_keys, obstacles, screenSize):
        # print(f"player x: {self.pos_x}  y:{self.pos_y}")

        # Короче прикол таков, нужно мувмент чтобы был не 1 пиксель в тик а % от мапы в тик
        # self.pos_x *= pygame.display.get_surface().get_width() / 1024
        # self.pos_y *= pygame.display.get_surface().get_height() / 768

        self.animation_cooldown -= 1
        if self.animation_cooldown == 0:
            self.animation_cooldown = 8
            self.animation_tick += 1

        if self.animation_tick > 4:
            self.animation_tick = 1

        if(not pressed_keys[pygame.K_w] and not pressed_keys[pygame.K_a] and not pressed_keys[pygame.K_s] and not pressed_keys[pygame.K_d]):
            self.currentTexture = pygame.image.load(self.bottom.get(1))
            return

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
            self.locationHandler.setCurrentLocation(self.locationHandler.getLeftLocation().getName())
            print("reached LEFT end")
            self.pos_x = screenSize[0] - self.width * 2
        if self.pos_x + self.width * 2 > screenSize[0]:  # REDO
            self.locationHandler.setCurrentLocation(self.locationHandler.getRightLocation().getName())
            print("reached RIGHT end")
            self.pos_x = 0
        if self.pos_y < 0:
            self.locationHandler.setCurrentLocation(self.locationHandler.getTopLocation().getName())
            print("reached TOP end")
            self.pos_y = screenSize[1] - self.height * 2
        if self.pos_y + self.height * 2 > screenSize[1]:  # REDO
            self.locationHandler.setCurrentLocation(self.locationHandler.getBottomLocation().getName())
            print("reached BOTTOM end")
            self.pos_y = 0

    def getLocationHandler(self):
        return self.locationHandler
