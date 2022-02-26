
# import libraries
import utils
from utils import Tile
import pygame
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

# initialise game
pygame.init()
screen, SCREEN_HEIGHT, SCREEN_WIDTH = utils.create_screen()

# images
# Tiles
# Tile naming convention
""" For the numbered suits the image is named with a number then the letter of the suit """
""" For the winds and dragons the image is saved a singular letter """
# aspect ratio that was ideal was 600 to 45 and 800 to 35

image_ratio_w = 35.0/800
image_ratio_h = 60.0/600

tile_backing = pygame.image.load('./mahjong-tiles/back.jpg')
#tile_width,tile_height = tile_backing.get_size()
tile_width = SCREEN_WIDTH*image_ratio_w
tile_height = SCREEN_HEIGHT*image_ratio_h
tile_backing = pygame.transform.scale(tile_backing,(tile_width,tile_height))
for i in range(18):
    screen.blit(tile_backing,(SCREEN_WIDTH/2-tile_width*9+i*tile_width,SCREEN_HEIGHT/7))

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

# Player 1 tile display
# not the best
image_ratio_w = 50.0/800
image_ratio_h = 80.0/600
tile_width = SCREEN_WIDTH*image_ratio_w
tile_height = SCREEN_HEIGHT*image_ratio_h
for i in range(len(players[0])):
    tiles = players[0][i]
    players_tiles = pygame.image.load('./mahjong-tiles/'+tiles.suit_type + tiles.value+'.jpg')
    players_tiles = pygame.transform.scale(players_tiles,(tile_width,tile_height))
    screen.blit(players_tiles,(SCREEN_WIDTH/2 - tile_width*6.5+ i*tile_width,SCREEN_HEIGHT-tile_height-40))

pygame.display.update()

# check statements
ping_hu_tiles = []
for i in range(4):
    ping_hu_tiles.append(Tile("Bamboo", "1"))
    ping_hu_tiles.append(Tile("Bamboo", "2"))
    ping_hu_tiles.append(Tile("Bamboo", "4"))
ping_hu_tiles.append(Tile("Bamboo", "5"))
ping_hu_tiles.append(Tile("Bamboo", "5"))
print(utils.check_for_pinghu(ping_hu_tiles))
# utils.print_tiles(players[0])
# print(len(all_tiles))
# print(utils.check_for_chi(players[0], Tile("Circles", "3")))
# for i in range(14):
#     tiles = ping_hu_tiles[i]
#     players_tiles = pygame.image.load('./mahjong-tiles/'+tiles.suit_type + tiles.value+'.jpg')
#     players_tiles = pygame.transform.scale(players_tiles,(tile_width,tile_height))
#     screen.blit(players_tiles,(SCREEN_WIDTH/2.0 - tile_width*6.5+ i*tile_width,SCREEN_HEIGHT-tile_height-40))

# pygame.display.update()
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
