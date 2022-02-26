
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
