
import utils
import pygame

tile_backing = pygame.image.load('./mahjong-tiles/back.jpg')
tile_width,tile_height = tile_backing.get_size()
tile_backing = pygame.transform.scale(tile_backing,(tile_width,tile_height))
for i in range(18):
    screen.blit(tile_backing,(100+i*tile_width,100))

pygame.display.update()
# Tile print
# not the best
for i in range(13):
    tiles = players[0][i]
    players_tiles = pygame.image.load('./mahjong-tiles/'+tiles.suit_type + tiles.value+'.jpg')
    players_tiles = pygame.transform.scale(players_tiles,(tile_width,tile_height))
    screen.blit(players_tiles,(100+i*tile_width,pygame.display.Info().current_h-100))

pygame.display.update()