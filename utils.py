import random
import pygame
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

def create_screen():
    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    display_info = pygame.display.Info()   
    SCREEN_HEIGHT = display_info.current_h
    SCREEN_WIDTH = display_info.current_w
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
    return all_tiles, []

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

def print_tiles(tiles_list):
    tiles_to_print = []
    for i in range(len(tiles_list)):
        tile = tiles_list[i]
        tiles_to_print.append(tile.suit_type + tile.value)
    print(tiles_to_print)

def sort_tiles(player_tiles):
    tiles_sorted = sorted(player_tiles, key = lambda x: (x.suit_type, x.value), reverse = False)
    return tiles_sorted

def check_for_chi(player_tiles, discarded_tile):
    wanted_tiles = []
    for i in range(5):
        wanted_tiles.append(Tile(discarded_tile.suit_type, str(int(discarded_tile.value) - 2 + i)))
    new_tile_set = player_tiles
    new_tile_set.append(discarded_tile)
    for i in range(3):
        if (wanted_tiles[i] in new_tile_set) and (wanted_tiles[i+1] in new_tile_set) and (wanted_tiles[i+2] in new_tile_set):
            return True
    return False

def check_for_peng(player_tiles, discarded_tile):
    count = 0
    for i in range(len(player_tiles)):
        if player_tiles[i] == discarded_tile:
            count += 1
    if count >= 3:
        return True
    else:
        return False

def check_for_gong(player_tiles, discarded_tile):
    count = 0
    for i in range(len(player_tiles)):
        if player_tiles[i] == discarded_tile:
            count += 1
    if count == 4:
        return True
    else:
        return False

def check_for_win(player_tiles):
    ping_hu = check_for_pinghu(player_tiles)
    peng_peng_hu = False
    ji_hu = False
    ban_se = False
    qing_yi_se = False
    yao_jiu = False
    shisan_yao = False
    #flower_hu = False
    win = ping_hu or peng_peng_hu or ji_hu or ban_se or qing_yi_se or yao_jiu or shisan_yao #or flower_hu
    return win

def check_for_pair(tile1, tile2):
    return tile1 == tile2

def check_for_pinghu(player_tiles):
    tiles_to_check = player_tiles
    count = 0
    while len(tiles_to_check) != 0 and count < 5:
        if len(tiles_to_check) == 2:
            if check_for_pair:
                return True
            else:
                return False
        else:
            tile1 = tiles_to_check[0]
            tile2 = Tile(tile1.suit_type, str(int(tile1.value)+1))
            tile3 = Tile(tile1.suit_type, str(int(tile1.value)+2))
            if tile1 in tiles_to_check and tile2 in tiles_to_check and tile3 in tiles_to_check:
                tiles_to_check.remove(tile1)
                tiles_to_check.remove(tile2)
                tiles_to_check.remove(tile3)
        count += 1
    return False
