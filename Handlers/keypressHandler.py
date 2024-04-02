import pygame

import Player
import main


def handleKeypress(pressed_keys):
    if pressed_keys[pygame.K_w]:
        main.Game.player.moveRelative((0, -1))
    if pressed_keys[pygame.K_a]:
        main.Game.player.moveRelative((-1, 0))
    if pressed_keys[pygame.K_s]:
        main.Game.player.moveRelative((0, 1))
    if pressed_keys[pygame.K_d]:
        main.Game.player.moveRelative((1, 0))




