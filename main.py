
# import libraries
import utils
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
# aspect ratio that was ideal was 600 to 45 and 800 to 35

tile_backing = pygame.image.load('./mahjong-tiles/back.jpg')
tile_width,tile_height = tile_backing.get_size()
tile_backing = pygame.transform.scale(tile_backing,(tile_width,tile_height))
for i in range(18):
    screen.blit(tile_backing,(100+i*tile_width,100))

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


# Card class definition
class Tile:
    def __init__(self, suit_type, value):
        self.suit_type = suit_type
        self.value = value

    def __eq__(self, other):
        return (self.suit_type == other.suit_type) and (self.value == other.value)

    def __lt__(self, other):
        return self.suit_type < other.suit_type


# check statements
utils.print_tiles(players[0])
print(len(all_tiles))
print(utils.check_for_chi(players[0], Tile("Circles", "3")))

# Variable to keep the main loop running
running = True

# Tile print
# not the best
for i in range(13):
    tiles = players[0][i]
    players_tiles = pygame.image.load('./mahjong-tiles/'+tiles.suit_type + tiles.value+'.jpg')
    players_tiles = pygame.transform.scale(players_tiles,(tile_width,tile_height))
    screen.blit(players_tiles,(100+i*tile_width,pygame.display.Info().current_h-100))

pygame.display.update()

# for mouse
# Mouse_x, Mouse_y = pygame.mouse.get_pos()
# key = pygame.key.get_pressed()

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
