# import libraries
import utils
import pygame

# Aspect ratio
# aspect ratio that was ideal was 600 to 45 and 800 to 35
image_ratio_w = 40.0/800
image_ratio_h = 50.0/600

# images
# Tiles
# Tile naming convention
""" For the numbered suits the image is named with a number then the letter of the suit """
""" For the winds and dragons the image is saved a singular letter """

# unused tiles generation and display
tile_backing = pygame.image.load('./mahjong-tiles/back.jpg')
tile_width= image_ratio_w*SCREEN_WIDTH
tile_height = image_ratio_h*SCREEN_HEIGHT
tile_backing = pygame.transform.scale(tile_backing,(tile_width*image_ratio_w,tile_height*image_ratio_h))
for i in range(18):
    screen.blit(tile_backing,(100+i*tile_width,100))

pygame.display.update()

# Player 1 tile display
# not the best
for i in range(13):
    tiles = players[0][i]
    players_tiles = pygame.image.load('./mahjong-tiles/'+tiles.suit_type + tiles.value+'.jpg')
    players_tiles = pygame.transform.scale(players_tiles,(tile_width,tile_height))
    screen.blit(players_tiles,(100+i*tile_width,pygame.display.Info().current_h-100))

pygame.display.update()