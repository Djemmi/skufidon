# import pygame
#
# from Handlers import keypressHandler
# from Player import Player
# from obstacle import Obstacle
# pygame.init()
#
# WIDTH = 800
# HEIGHT = 600
# NET_GAP = 50
#
# # COORDINATES
# player = Player(WIDTH // 2, HEIGHT // 2)
#
# test_obstacle = Obstacle((500, 200), 150, 50, {})
#
# player_speed = 1
# location_color = (255, 0, 0)
#
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
#
# running = True
#
#
# def swap_location(location_color) -> tuple:
#     if location_color == (255, 0, 0):
#         return (0, 255, 0)
#     elif location_color == (0, 255, 0):
#         return (255, 0, 0)
#     return (255, 255, 255)
#
# while running:
#     screen.fill((0, 0, 0))
#     for x in range(NET_GAP, WIDTH, NET_GAP):
#             pygame.draw.line(screen, location_color, (x, 0), (x, HEIGHT))
#     for y in range(NET_GAP, HEIGHT, NET_GAP):
#             pygame.draw.line(screen, location_color, (0, y), (WIDTH, y))
#
#     pygame.draw.rect(screen, (0, 0, 255), test_obstacle.getRect())
#
#
#
#     pressed_keys = pygame.key.get_pressed()
#
#     # HANDLE KEY PRESSING
#     keypresshandler.handlePressedKeys(pressed_keys, player)
#
#     if(test_obstacle.isTouching(player.getPosition())):
#         print("TOUCHING PLAYER")
#
#
#     # map endings
#     if player.getX() > WIDTH - 25:
#         location_color = swap_location(location_color)
#         player.setX(25)
#     if player.getX() < 25:
#         location_color = swap_location(location_color)
#         player.setX(WIDTH - 25)
#     if player.getY() > HEIGHT - 25:
#         location_color = swap_location(location_color)
#         player.setY(25)
#     if player.getY() < 25:
#         location_color = swap_location(location_color)
#         player.setY(HEIGHT - 25)
#
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     pygame.draw.circle(screen, (0, 150, 150), (player.getX(), player.getY()), 25)
#     pygame.display.flip()
#
# pygame.quit()
#
#
from MainThread import MainThread

Game = MainThread()
Game.startGame()

