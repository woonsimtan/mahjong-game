# import libraries
from pickle import FALSE, TRUE
from traceback import print_list
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import pygame.gfxdraw
import utils
from utils import Tile, print_tiles_as_str
from random import randint
import time


# initialise game
pygame.init()
screen, SCREEN_HEIGHT, SCREEN_WIDTH = utils.create_screen()

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


# # check statements
# hu_tiles = []
# for i in range(3):
#     hu_tiles.append(Tile("Bamboo", "1"))
#     hu_tiles.append(Tile("Bamboo", "9"))
#     hu_tiles.append(Tile("Circles", "2"))
#     hu_tiles.append(Tile("Circles", "9"))
# hu_tiles.append(Tile("Numbers", "1"))
# hu_tiles.append(Tile("Numbers", "1"))
# print(utils.check_for_yaojiu(hu_tiles))
# print(utils.check_for_win(hu_tiles))
# # utils.print_tiles(players[0])
# # print(len(all_tiles))
# # print(utils.check_for_chi(players[0], Tile("Circles", "3")))
# # for i in range(14):
# #     tiles = ping_hu_tiles[i]
# #     players_tiles = pygame.image.load('./mahjong-tiles/'+tiles.suit_type + tiles.value+'.jpg')
# #     players_tiles = pygame.transform.scale(players_tiles,(tile_width,tile_height))
# #     screen.blit(players_tiles,(screen_width/2.0 - tile_width*6.5+ i*tile_width,screen_height-tile_height-40))

# # pygame.display.update()
# # Variable to keep the main loop running
RUNNING = True
player = 2
# pos = 0

utils.player_graphics(players[0], screen)
utils.comp_graphics(screen)
new = True
# Main loop
while RUNNING and len(all_tiles) > 0:

    # TODO: utils.print_wall(screen)

    # Loop events occuring inside the game window

    if player == 0:
        utils.player_graphics(players[player], screen)
        if new:
            # print(len(all_tiles))
            new_tile = utils.pick_up_tile(all_tiles)
            players[player].append(new_tile)
            all_tiles.remove(new_tile)
            # print(len(all_tiles))
            players[player] = utils.sort_tiles(players[player])
            new = False
    else:
        time.sleep(1)
        new_tile = utils.pick_up_tile(all_tiles)
        players[player].append(new_tile)
        all_tiles.remove(new_tile)
        discard_tile = players[player][randint(0, 13)]
        players[player].remove(discard_tile)
        discarded_tiles.append(discard_tile)
        utils.discard_graphics(screen, discard_tile, discarded_tiles)
        player = (player + 1) % 4
        new = True

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False
        elif event.type == QUIT:
            RUNNING = False
        # TODO: if mouse is hovered on a tile highlight the tile
        # TODO: check for pong/kong/chi
        if player == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if event.button == 1:
                    pos = utils.tile_coordinates(mouse)
                    if isinstance(pos, int):
                        # utils.print_tiles_as_str(players[0])
                        # utils.print_tiles_as_str([players[0][pos]])
                        discarded_tiles.append(players[0][pos])

                        utils.discard_graphics(screen, players[0][pos], discarded_tiles)

                        players[0].remove(players[0][pos])
                        utils.clear_screen(screen, discarded_tiles)
                        utils.player_graphics(players[0], screen)
                        player = (player + 1) % 4
                        new = True


# Resizable window
# if event.type == pygame.VIDEORESIZE:
#     # There's some code to add back window content here.
#     screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

#     utils.player_graphics(players, screen, 0)
#     utils.comp_graphics(screen)

# mouse = pygame.mouse.get_pos()
# pos = utils.tile_coordinates(mouse, screen)
# if pos is int:
#     utils.player_graphics(players, screen, pos)

# if pygame.MOUSEBUTTONDOWN:
#     #     pos = utils.tile_coordinates(mouse, screen)
#     discarded_tiles.append(players[0][pos])
# # utils.print_tiles_as_str(discarded_tiles)
# for i in range(4):
#     players[i].append
# pos = pygame.mouse.get_pos()
# if event.type == pygame.VIDEORESIZE:
#     width, height = event.dict["size"]
#     # recreate screen object required for pygame version 1
#     screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
