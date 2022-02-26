# import libraries
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

import utils
from utils import Tile

# initialise game
pygame.init()
screen, screen_height, screen_width = utils.create_screen()

# images
# Tiles
# Tile naming convention
""" For the numbered suits the image named with number + suit letter """
""" For the winds and dragons the image is saved a singular letter """
# aspect ratio that was ideal was 600 to 45 and 800 to 35


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

# Player 1 tile display
# not the best


# check statements
hu_tiles = []
for i in range(3):
    hu_tiles.append(Tile("Bamboo", "1"))
    hu_tiles.append(Tile("Bamboo", "9"))
    hu_tiles.append(Tile("Circles", "2"))
    hu_tiles.append(Tile("Circles", "9"))
hu_tiles.append(Tile("Numbers", "1"))
hu_tiles.append(Tile("Numbers", "1"))
print(utils.check_for_yaojiu(hu_tiles))
print(utils.check_for_win(hu_tiles))
# utils.print_tiles(players[0])
# print(len(all_tiles))
# print(utils.check_for_chi(players[0], Tile("Circles", "3")))
# for i in range(14):
#     tiles = ping_hu_tiles[i]
#     players_tiles = pygame.image.load('./mahjong-tiles/'+tiles.suit_type + tiles.value+'.jpg')
#     players_tiles = pygame.transform.scale(players_tiles,(tile_width,tile_height))
#     screen.blit(players_tiles,(screen_width/2.0 - tile_width*6.5+ i*tile_width,screen_height-tile_height-40))

# pygame.display.update()
# Variable to keep the main loop running
RUNNING = True

# Main loop
while RUNNING:
    # Tracking the mouse movements
    mouse = pygame.mouse.get_pos()
    utils.print_wall(screen)
    utils.player_graphics(players, screen)
    # Loop events occuring inside the game window
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                RUNNING = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            RUNNING = False
