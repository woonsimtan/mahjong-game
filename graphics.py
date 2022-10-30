import pygame
import math
import time


def create_screen():
    # Create the screen object
    # The size is determined by the constant screen_width and screen_height
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.toggle_fullscreen()
    display_info = pygame.display.Info()
    SCREEN_HEIGHT = display_info.current_h
    SCREEN_WIDTH = display_info.current_w
    GREEN = (0, 105, 53)
    WHITE = (255, 255, 255)
    screen.fill(GREEN)
    pygame.display.update()

    # Setting up caption
    pygame.display.set_caption("Mahjong Game")

    # Loading image for the icon
    icon = pygame.image.load("icon.jpg")

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
    return screen, SCREEN_HEIGHT, SCREEN_WIDTH


def size_values(width, height):
    display_info = pygame.display.Info()
    SCREEN_HEIGHT = display_info.current_h
    SCREEN_WIDTH = display_info.current_w
    image_ratio_w = width / 800
    image_ratio_h = height / 600
    tile_width = SCREEN_WIDTH * image_ratio_w
    tile_height = SCREEN_HEIGHT * image_ratio_h
    return tile_width, tile_height


# Player 1 tile display
def player_one_graphics(player_one, screen):
    display_info = pygame.display.Info()
    SCREEN_HEIGHT = display_info.current_h
    SCREEN_WIDTH = display_info.current_w
    tile_width, tile_height = size_values(50.0, 80.0)
    for i in range(len(player_one)):

        tiles = player_one[i]
        players_tiles = pygame.image.load(
            "./mahjong-tiles/" + tiles.suit_type + tiles.value + ".jpg"
        )
        # Attempt at making the selected tile shift up
        # if i != pos:
        #     players_tiles = pygame.transform.scale(
        #         players_tiles, (tile_width, tile_height)
        #     )
        #     screen.blit(
        #         players_tiles,
        #         (
        #             SCREEN_WIDTH / 2 - tile_width * 6.5 + i * tile_width,
        #             SCREEN_HEIGHT - tile_height - 40,
        #         ),
        #     )
        # else:
        players_tiles = pygame.transform.scale(players_tiles, (tile_width, tile_height))
        screen.blit(
            players_tiles,
            (
                SCREEN_WIDTH / 2.0 - tile_width * 7 + i * tile_width,
                SCREEN_HEIGHT - tile_height - 60,
            ),
        )

    pygame.display.update()


def discard_graphics(screen, tiles, discarded_tiles):
    display_info = pygame.display.Info()
    SCREEN_HEIGHT = display_info.current_h
    SCREEN_WIDTH = display_info.current_w
    tile = pygame.image.load(
        "./mahjong-tiles/" + tiles.suit_type + tiles.value + ".jpg"
    )
    tile_width, tile_height = size_values(25.0, 45.0)
    tile = pygame.transform.scale(tile, (tile_width, tile_height))
    # The row and column determined is from the fact that there are 148 Mahjong tiles
    # If there is a draw then there will be 96 tiles left
    total_row = 8
    total_column = 12

    tile_pos = len(discarded_tiles) - 1
    tile_row = tile_pos // total_column
    tile_column = tile_pos % total_column
    margin_left = SCREEN_WIDTH / 2 - (total_column / 2) * tile_width
    margin_top = SCREEN_HEIGHT / 2 - (total_row / 2) * tile_height
    pos_width = margin_left + tile_width * tile_column
    pos_height = margin_top + tile_height * tile_row
    screen.blit(tile, (pos_width, pos_height))

    pygame.display.update()


def comp_graphics(screen):
    display_info = pygame.display.Info()
    SCREEN_HEIGHT = display_info.current_h
    SCREEN_WIDTH = display_info.current_w
    tile_width, tile_height = size_values(30.0, 50.0)
    tile_backing = pygame.image.load("./mahjong-tiles/back.jpg")
    tile_backing = pygame.transform.scale(tile_backing, (tile_width, tile_height))
    tile_backing_sides = pygame.transform.rotate(tile_backing, 90)
    for i in range(3):
        if i == 1:
            for j in range(13):
                screen.blit(
                    tile_backing,
                    (
                        SCREEN_WIDTH / 2 - tile_width * 6.5 + j * tile_width,
                        0,
                    ),
                )
        else:
            for j in range(13):
                if i // 2 == 1:
                    screen.blit(
                        tile_backing_sides,
                        (
                            SCREEN_WIDTH - tile_height,
                            SCREEN_HEIGHT / 2 - 6.5 * tile_width + j * tile_width,
                        ),
                    )
                else:
                    screen.blit(
                        tile_backing_sides,
                        (
                            0,
                            SCREEN_HEIGHT / 2 - 6.5 * tile_width + j * tile_width,
                        ),
                    )
    pygame.display.update()


def tile_coordinates(coord):
    display_info = pygame.display.Info()
    SCREEN_HEIGHT = display_info.current_h
    SCREEN_WIDTH = display_info.current_w
    tile_width, tile_height = size_values(50.0, 80.0)
    margin_left = SCREEN_WIDTH / 2 - 7 * tile_width
    margin_top = SCREEN_HEIGHT - tile_height - 60
    margin_right = margin_left + tile_width * 14
    if (
        coord[0] >= margin_left
        and coord[0] < margin_right
        and coord[1] >= margin_top
        and coord[1] < margin_top + tile_height
    ):
        return int(math.floor((coord[0] - margin_left) // tile_width))


def clear_screen(screen, discarded_tiles):
    GREEN = (0, 105, 53)
    display_info = pygame.display.Info()
    tile_width, tile_height = size_values(50.0, 80.0)
    margin_top = display_info.current_h - tile_height - 60
    margin_right = display_info.current_w / 2 - 7 * tile_width + tile_width * 13
    screen.fill(GREEN, (margin_right, margin_top, tile_width, tile_height))
    comp_graphics(screen)
    discard_graphics(screen, discarded_tiles[-1], discarded_tiles)
    return screen


def genereate_buttons(screen, peng, gong, chi):
    display_info = pygame.display.Info()
    SCREEN_HEIGHT = display_info.current_h
    SCREEN_WIDTH = display_info.current_w

    # Types of fonts to be used
    large_font = pygame.font.SysFont("arial", 50)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Game Buttons
    peng_button = large_font.render("Peng", True, WHITE)
    gong_button = large_font.render("Gong", True, WHITE)
    chi_button = large_font.render("Chi", True, WHITE)
    # hu_button = large_font.render("Hu", True, WHITE)

    # Gets_rectangular covering of text
    peng_button_rect = peng_button.get_rect()
    gong_button_rect = gong_button.get_rect()
    chi_button_rect = chi_button.get_rect()
    # hu_button_rect = hu_button.get_rect()

    tile_height = 80  # edit this!
    # Places the text
    peng_button_rect.center = (
        SCREEN_WIDTH - 2 * tile_height,
        SCREEN_HEIGHT - 2 * tile_height,
    )
    gong_button_rect.center = (
        SCREEN_WIDTH - 3 * tile_height,
        SCREEN_HEIGHT - 2 * tile_height,
    )
    chi_button_rect.center = (
        SCREEN_WIDTH - 4 * tile_height,
        SCREEN_HEIGHT - 2 * tile_height,
    )
    # hu_button_rect.center = (SCREEN_WIDTH - 5 *tile_height, SCREEN_HEIGHT - 2*tile_height)
    if peng:
        screen.blit(peng_button, peng_button_rect)
    if gong:
        screen.blit(gong_button, gong_button_rect)
    if chi:
        screen.blit(chi_button, chi_button_rect)
    # screen.blit(hu_button, hu_button_rect)
    pygame.display.update()