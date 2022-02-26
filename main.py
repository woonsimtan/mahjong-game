
# import libraries
import utils
from utils import Tile
import pygame
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

# initialise game
pygame.init()
screen = utils.create_screen()

# images
# Tiles
# Tile naming convention
""" For the numbered suits the image is named with a number then the letter of the suit """
""" For the winds and dragons the image is saved a singular letter """

tile_height = 45
tile_width = 35
Tile_backing = pygame.image.load('./mahjong-tiles/back.jpg')
Tile_backing = pygame.transform.scale(Tile_backing,(tile_width,tile_height))
# screen.blit(Tile_backing,(100,100))
for i in range(18):
    screen.blit(Tile_backing,(100+i*tile_width,100))

pygame.display.update()

# The type of card
# TODO: add flowers
suit_values = {
    "Numbers": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "Circles": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "Bamboo": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "Wind": ["N", "S", "W", "E"],
    "Dragon": ["B", "Z", "F"],
    # "Flower": [["1", "2", "3", "4", "5", "6", "7", "8"]
}
# The card value - for counting points
# tile_values = {
#     "1": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, 
#     "E":10, "S": 11, "W":12, "N":13, 
#     "B":20, "Z":21, "F":22
# }

# The mahjong tiles - List of Objects
all_tiles, discarded_tiles = utils.create_tiles(suit_values)
# set up players
players, all_tiles = utils.distribute_tiles(all_tiles)

# check statements
hu_tiles = []
for i in range(3):
    hu_tiles.append(Tile("Bamboo", "1"))
    hu_tiles.append(Tile("Bamboo", "2"))
    hu_tiles.append(Tile("Bamboo", "4"))
    hu_tiles.append(Tile("Bamboo", "6"))
hu_tiles.append(Tile("Bamboo", "5"))
hu_tiles.append(Tile("Bamboo", "5"))
print(utils.check_for_pengpenghu(hu_tiles))
print(utils.check_for_win(hu_tiles))
# utils.print_tiles(players[0])
# print(len(all_tiles))
# print(utils.check_for_chi(players[0], Tile("Circles", "3")))

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Tracking the mouse movements
    mouse = pygame.mouse.get_pos()
    # Loop events occuring inside the game window 
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
