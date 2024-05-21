import pygame
from pygame import *
import logging
import screeninfo

from Entities.Entities.Player import Player
from Handlers.eventHandler import eventHandler

from enums.Colors import Color


# TODO HUGE FUCKING TODO, REMOVE THIS CLASS prob idk we could just use instance from main but it sucks tbh
class MainThread:

    def __init__(self):

        self.currentLocationTexture = None
        self.currentLocation = None
        self.running = True  # to prevent some runtime errors nvm
        self.eventHandler = eventHandler()

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(name)s - %(message)s"
        )

        self.logger = logging.getLogger("MainThread")

    def preInit(self) -> None:

        """

        Some theory here
        Our game basic resolutoin is 1024x768 (XGA)

        """

        self.logger.info("Running pre init")
        # I dont like this one, wont use KEKW
        self.screenWidth = 800
        self.screenHeight = 600

        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        self.unscaledScreen = Surface((800, 600))
        self.clock = pygame.time.Clock()  # what do we need this for
        self.player = Player((self.unscaledScreen.get_width() // 2, self.unscaledScreen.get_width() // 2))

    # def initTextures(self) -> None:
    #     # Init locations
    #     # Obstacles should be inited in init method of location class
    #
    #     # loading current textures

    def startGame(self):

        self.preInit()
        # main game loop
        while self.isRunning():
            self.widthScaling = pygame.display.get_surface().get_width() / 1024
            self.heightScaling = pygame.display.get_surface().get_height() / 768

            # this line have to be on top of this loop
            self.unscaledScreen.fill((113, 169, 44))
            # TODO return background
            self.currentLocation = self.player.getLocationHandler().getCurrentLocation()
            # self.logger.info(f"LOCA {self.currentLocation.getName()}")
            # self.logger.info(f"obstacles: {self.currentLocation.getObstacles()}")
            self.currentLocationTexture = pygame.transform.scale(pygame.image.load(self.currentLocation.texture), (self.unscaledScreen.get_width(), self.unscaledScreen.get_height()))
            self.unscaledScreen.blit(self.currentLocationTexture, (0, 0))

            events = pygame.event.get()
            pressed_keys = pygame.key.get_pressed()

            # Handling all information in other classes
            self.eventHandler.register(self.stopGame, pygame.QUIT)
            self.eventHandler.handleEvents(events)
            self.player.handleActions(pressed_keys, self.currentLocation.getObstacles(),
                                      (self.unscaledScreen.get_width(), self.unscaledScreen.get_height()))

            for obj in self.currentLocation.getObstacles():
                if obj.getCurrentTexture() is None:
                    self.logger.info("Missing texture for object " + obj.getName())
                    self.logger.info("Please contact devs if you see this ERROR:MISSING_OBSTACLE_TEXTURE")
                    break
                if obj.hasAnimation():
                    obj.playAnimation()

                pygame.draw.line(self.unscaledScreen, Color.RED.value, (self.player.getX(), self.player.getY()), (obj.getX(), obj.getY()))
                self.unscaledScreen.blit(obj.getCurrentTexture(), (obj.getX(), obj.getY()))

                # Draw hit-boxes, comment if you don't need this
                pygame.draw.line(self.unscaledScreen, Color.RED.value, (obj.getX(), obj.getY()),
                                 (obj.getX() + obj.getWidth(), obj.getY()))
                pygame.draw.line(self.unscaledScreen, Color.RED.value, (obj.getX(), obj.getY()),
                                 (obj.getX(), obj.getY() + obj.getHeight()))
                pygame.draw.line(self.unscaledScreen, Color.RED.value, (obj.getX(), obj.getY() + obj.getHeight()),
                                 (obj.getX() + obj.getWidth(), obj.getY() + obj.getHeight()))
                pygame.draw.line(self.unscaledScreen, Color.RED.value, (obj.getX() + obj.getWidth(), obj.getY()),
                                 (obj.getX() + obj.getWidth(), obj.getY() + obj.getHeight()))

            self.unscaledScreen.blit(self.player.getCurrentTexture(), (self.player.getX(), self.player.getY()))

            pygame.draw.line(self.unscaledScreen, Color.RED.value, (self.player.getX(), self.player.getY()),
                             (self.player.getX() + self.player.getWidth(), self.player.getY()))
            pygame.draw.line(self.unscaledScreen, Color.RED.value, (self.player.getX(), self.player.getY()),
                             (self.player.getX(), self.player.getY() + self.player.getHeight()))
            pygame.draw.line(self.unscaledScreen, Color.RED.value,
                             (self.player.getX(), self.player.getY() + self.player.getHeight()),
                             (self.player.getX() + self.player.getWidth(), self.player.getY() + self.player.getHeight()))
            pygame.draw.line(self.unscaledScreen, Color.RED.value,
                             (self.player.getX() + self.player.getWidth(), self.player.getY()),
                             (self.player.getX() + self.player.getWidth(), self.player.getY() + self.player.getHeight()))

            self.scaledScreen = transform.scale(self.unscaledScreen, (self.screen.get_width(), self.screen.get_height()))
            print((self.screen.get_width(), self.screen.get_height()))
            self.screen.blit(self.scaledScreen, (0, 0))

            # these lines are last, club't change that
            pygame.display.flip()
            self.clock.tick(120)

    def isRunning(self):
        return self.running

    def stopGame(self):
        self.logger.info("Stopping game. Cya!")
        self.running = False
        pygame.quit()
        exit(0)

    def getEventHandler(self):
        return self.eventHandler

    def setResolution(self, size):
        self.screenWidth = size[0]
        self.screenHeight = size[1]