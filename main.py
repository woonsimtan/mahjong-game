
# import and initialise python
import pygame
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
table_GREEN = (0 ,105, 53)
WHITE = (255, 255, 255)
screen.fill(table_GREEN)
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


# Card class definition
class Tile:
    def __init__(self, suit_type, value):
        self.suit_type = suit_type
        self.value = value

# The type of suit
suits = ["Numbers", "Circles", "Bamboo", "Dragon", "Wind"]
 
# The type of card
tiles = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "N", "S", "W", "E", "B", "Z", "F"]
 
# The card value
tile_values = {"1": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, 
                "E":10, "S": 11, "W":12, "N":13, 
                "B":20, "Z":21, "F":22}
# TODO: add flowers

# The deck of cards - List of Objects
all_tiles = []
 
# Loop for every type of suit
for suit in suits:
    # Loop for every type of card in a suit
    for tile in tiles:
        # Add 4 of each tile
        for i in range(4):
            # Adding the card to the deck
            all_tiles.append(Tile(suit, tile))



# Variable to keep the main loop running
running = True

# for mouse
# Mouse_x, Mouse_y = pygame.mouse.get_pos()
# key = pygame.key.get_pressed()

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
