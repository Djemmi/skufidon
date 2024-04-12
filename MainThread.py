import pygame
import logging
import screeninfo

from Handlers.eventHandler import eventHandler
from Location.Locations.Limbo import Limbo
from Location.Locations.TestLocation import TestLocation
from enums.colors import Color
import Player


class MainThread:
    player = None
    screenWidth = None
    clock = None
    screen = None
    screenHeight = None
    currentLocation = None
    currentLocationTexture = None
    TestLocaiton = None
    Limbo = None

    def __init__(self):
        # TODO check if we really need to init these vars here

        self.running = True  # to prevent some runtime errors nvm
        self.eventHandler = eventHandler()

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(name)s - %(message)s"
        )

        self.logger = logging.getLogger("MainThread")

    def preInit(self) -> None:

        self.logger.info("Running pre init")
        self.screenWidth = screeninfo.get_monitors()[0].width
        self.screenHeight = screeninfo.get_monitors()[0].height
        self.screen = pygame.display.set_mode((800, 600 ))  # TODO work with screen resolution
        self.clock = pygame.time.Clock()  # what do we need this for
        self.player = Player.Player(self.screen.get_width() // 2, self.screen.get_height() // 2)

    def initTextures(self) -> None:
        # Init locations
        # Obstacles should be inited in init method of location class
        self.testLocation = TestLocation()
        self.Limbo = Limbo()

        # loading current textures
        self.currentLocation = self.testLocation
        self.currentLocationTexture = pygame.image.load(self.currentLocation.texture)

    def startGame(self):
        self.preInit()
        self.initTextures()
        # main game loop
        while self.isRunning():
            self.logger.info("GameTick")
            # this line have to be on top of this loop
            self.screen.fill((113,169,44))
            # TODO return background
            # self.screen.blit(self.currentLocationTexture, (0, 0))

            events = pygame.event.get()
            pressed_keys = pygame.key.get_pressed()

            # Handling all information in other classes
            self.eventHandler.register(self.stopGame, pygame.QUIT)
            self.eventHandler.handleEvents(events)
            self.player.handleActions(pressed_keys, self.currentLocation.getObstacles())

            NET_GAP = 50
            # Draw objects here
            for x in range(NET_GAP, self.screenWidth, NET_GAP):
                pygame.draw.line(self.screen, Color.BLACK.value, (x, 0), (x, self.screenHeight))
            for y in range(NET_GAP, self.screenHeight, NET_GAP):
                pygame.draw.line(self.screen, Color.BLACK.value, (0, y), (self.screenWidth, y))

            self.logger.info(self.currentLocation)


            # TODO добавить инициализацию мапы {object: currentTexture} до начала цикла
            # TODO а лучше добавить еще один пунк инициализации initTextures для подгрузк в оперативу всех объектов локации (ПОДУМАТЬ НАД ЭТИМ)
            for obj in self.currentLocation.getObstacles():
                if obj.getCurrentTexture() is None:
                    self.logger.info("Missing texture for object " + obj.getName())
                    break
                obj.playAnimation()
                self.screen.blit(obj.getCurrentTexture(), obj.getPos())
                # Draw hit-boxes, comment if you don't need this
                pygame.draw.line(self.screen, Color.RED.value, (obj.getX(), obj.getY()), (obj.getX() + obj.getWidth(), obj.getY()))
                pygame.draw.line(self.screen, Color.RED.value, (obj.getX(), obj.getY()), (obj.getX(), obj.getY() + obj.getHeight()))
                pygame.draw.line(self.screen, Color.RED.value, (obj.getX(), obj.getY() + obj.getHeight()), (obj.getX() + obj.getWidth(), obj.getY() + obj.getHeight()))
                pygame.draw.line(self.screen, Color.RED.value, (obj.getX() + obj.getWidth(), obj.getY()), (obj.getX() + obj.getWidth(), obj.getY() + obj.getHeight()))

            pygame.draw.circle(self.screen, (0, 0, 255), self.player.getPosition(), 25, 2)

            # these lines are last, don't change that
            pygame.display.flip()
            self.clock.tick(60)

    # I NEED LOMBOK PLEASE GOOOOOD
    def isRunning(self):
        return self.running

    def stopGame(self):
        self.logger.info("Stopping game. Cya!")
        self.running = False
        pygame.quit()
        exit(0)
