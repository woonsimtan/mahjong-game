import pygame
import graphics
import gameplay_single as gameplay
import time
from pygame.locals import KEYDOWN, QUIT


# initialise game
pygame.init()
screen, SCREEN_HEIGHT, SCREEN_WIDTH = graphics.create_screen()

# fixed values
suit_values = {
    "Numbers": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "Circles": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "Bamboo": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "Wind": ["E", "S", "W", "N"],
    "Dragon": ["B", "Z", "F"],
}

flowers = {
    "A": ["1", "2", "3", "4"],
    "B": ["1", "2", "3", "4"],
}

round = 0
prevailing = "E"
player_number = 0  # change this to player who's position is east
all_tiles = gameplay.create_tiles()
players, all_tiles = gameplay.game_setup(all_tiles)
discarded_tiles = []
last_discarded = float("NaN")
running = True
new = True

graphics.player_one_graphics(players[0].hidden_tiles, screen)
graphics.comp_graphics(screen)

try:
    while not gameplay.check_for_win(last_discarded) and len(all_tiles) > 0 and running:

        if player_number == 0:
            graphics.player_one_graphics(players[player_number], screen)
            if new:
                new_tile = gameplay.pickup_tile(all_tiles)
                players[player_number].hidden_tiles.append(new_tile)
                new = False

        else:
            time.sleep(1)
            new_tile = gameplay.pickup_tile(all_tiles)
            players[player_number].hidden_tiles.append(new_tile)
            last_discarded = players[player_number].discard()
            graphics.discard_graphics(screen, last_discarded, discarded_tiles)
            player_number = (player_number + 1) % 4
            new = True

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

            if player_number == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if event.button == 1:
                        pos = graphics.tile_coordinates(mouse)
                        if isinstance(pos, int):
                            last_discarded = players[player_number].hidden_tiles[pos]
                            discarded_tiles.append(last_discarded)
                            graphics.discard_graphics(
                                screen, last_discarded, discarded_tiles
                            )
                            players[player_number].hidden_tiles.remove(last_discarded)
                            graphics.clear_screen(screen, discarded_tiles)
                            graphics.player_one_graphics(
                                players[player_number].hidden_tiles, screen
                            )
                            player = (player + 1) % 4
                            new = True

    if len(all_tiles) == 0:
        print("Nobody won")

except Exception as e:
    print(e)
