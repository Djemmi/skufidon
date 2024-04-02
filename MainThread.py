import pygame
import logging
import screeninfo

from Handlers.eventHandler import eventHandler
from Handlers.keypressHandler import handleKeypress
from enums.colors import Color
import Player


class MainThread:

    def __init__(self):
        # TODO check if we really need to init these vars here
        self.player = None
        self.screenWidth = None
        self.clock = None
        self.screen = None
        self.screenHeight = None

        self.running = True  # to prevent some runtime errors nvm
        self.eventHandler = eventHandler()

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(name)s - %(message)s"
        )

        self.logger = logging.getLogger("MainThread")

    def preInit(self):
        self.screen = pygame.display.set_mode((100, 100))  # TODO work with screen resolution
        self.clock = pygame.time.Clock()  # what do we need this for
        self.screenWidth = screeninfo.get_monitors()[0].width
        self.screenHeight = screeninfo.get_monitors()[0].height
        self.player = Player.Player(self.screenWidth // 2, self.screenHeight // 2)

    def startGame(self):
        self.preInit()
        # main game loop
        while self.isRunning():
            # this line have to be on top of this loop
            self.screen.fill(Color.BLACK)

            events = pygame.event.get()
            pressed_keys = pygame.key.get_pressed()

            # Handling all information in other classes
            eventHandler.register(self.stopGame(), pygame.QUIT)
            eventHandler.handleEvents(pygame.event.get())
            handleKeypress(pressed_keys)

            NET_GAP = 50
            # Draw objects here
            for x in range(NET_GAP, self.screenWidth, NET_GAP):
                    pygame.draw.line(self.screen, Color.GREEN, (x, 0), (x, self.screenHeight))
            for y in range(NET_GAP, self.screenHeight, NET_GAP):
                    pygame.draw.line(self.screen, Color.GREEN, (0, y), (self.screenWidth, y))

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
