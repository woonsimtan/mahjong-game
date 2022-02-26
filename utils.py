import random
import pygame
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

def create_screen():
# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    GREEN = (0 ,105, 53)
    WHITE = (255, 255, 255)
    screen.fill(GREEN)
    pygame.display.update()

    # Setting up caption
    pygame.display.set_caption("Mahjong Game")
    
    # Loading image for the icon
    icon = pygame.image.load('icon.jpg')
    
    # Setting the game icon
    pygame.display.set_icon(icon)

    # Types of fonts to be used
    small_font = pygame.font.Font(None, 32)
    large_font = pygame.font.Font(None, 50)

    # Game Buttons
    peng_button = large_font.render("碰", True, WHITE)
    gong_button = large_font.render("杠", True, WHITE)
    chi_button = large_font.render("吃", True, WHITE)
    hu_button = large_font.render("胡", True, WHITE)
    
    # Gets_rectangular covering of text
    peng_button_rect = peng_button.get_rect()
    gong_button_rect = gong_button.get_rect()
    chi_button_rect = chi_button.get_rect()
    hu_button_rect = hu_button.get_rect()
    
    # Places the text
    peng_button_rect.center = (280, 400)
    gong_button_rect.center = (360, 400)
    chi_button_rect.center = (440, 400)
    hu_button_rect.center = (520, 400)
    return screen

# Card class definition
class Tile:
    def __init__(self, suit_type, value):
        self.suit_type = suit_type
        self.value = value

    def __eq__(self, other):
        return (self.suit_type == other.suit_type) and (self.value == other.value)

    def __lt__(self, other):
        return self.suit_type < other.suit_type

def create_tiles(suit_values):
    all_tiles = []
    # Loop for every type of suit
    for key in suit_values.keys():
        # Loop for every type of card in a suit
        for i in suit_values[key]:
            # Add 4 of each tile
            for j in range(4):
                # Adding the card to the deck
                all_tiles.append(Tile(key, i))

    # shuffle tiles
    random.shuffle(all_tiles)
    return all_tiles

def distribute_tiles(all_tiles):
    players = [[],[],[],[]]
    # distribute tiles to players
    for i in range (3):
        for j in range(4):
            for k in range(4):
                players[j].append(all_tiles[j*4 + k])
        all_tiles = all_tiles[16:]
    for i in range(4):
        players[i].append(all_tiles[i])
        players[i] = sort_tiles(players[i])
    all_tiles = all_tiles[4:]
    return players, all_tiles

def print_player1(players):
    player1 = []
    for i in range(13):
        tile = players[0][i]
        player1.append(tile.suit_type + tile.value)
    print(player1)

def sort_tiles(player_tiles):
    tiles_sorted = sorted(player_tiles, key = lambda x: (x.suit_type, x.value), reverse = False)
    return tiles_sorted


    