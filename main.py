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
player_number = 0  # starting player
all_tiles = gameplay.create_tiles()
players, all_tiles = gameplay.game_setup(all_tiles)
discarded_tiles = []
last_discarded = float("NaN")
running = True
new = True
should_pass = False

if __name__ == "__main__":

    # initial display
    graphics.player_one_graphics(
        players[0].hidden_tiles, players[0].displayed_tiles, screen
    )
    graphics.comp_graphics(players, screen)

    while (
        not gameplay.check_for_win(players, last_discarded)
        and len(all_tiles) > 0
        and running
    ):
        if not should_pass:
            # check for peng
            peng, new_player_number = gameplay.check_for_peng(players, last_discarded)
            # BUG:should not be able to peng on tile that user discarded

            graphics.generate_buttons(
                screen, peng and (new_player_number == 0), False, False
            )
        else:
            peng = False
            new_player_number = float("NaN")

        if peng and new_player_number != 0:  # bots always assume peng if possible
            time.sleep(1)
            player_number = new_player_number
            players[player_number].peng(last_discarded)
            last_discarded = discarded_tiles.pop()

        if (peng and new_player_number != 0) or not peng:
            if player_number == 0:  # if user
                # display user tiles
                tiles = gameplay.sort_tile_list(players[player_number].hidden_tiles)
                graphics.player_one_graphics(tiles, players[0].displayed_tiles, screen)

                if new:  # if need to pick up a new tile
                    print("player " + str(player_number) + " picks up")
                    new_tile = gameplay.pickup_tile(all_tiles)
                    players[player_number].hidden_tiles.append(new_tile)
                    new = False

            else:
                # other players pick up a tile if did not peng
                if not peng:
                    time.sleep(1)
                    new_tile = gameplay.pickup_tile(all_tiles)
                    players[player_number].hidden_tiles.append(new_tile)
                    print("player " + str(player_number) + " picks up")

                # discard a random tile
                last_discarded = players[player_number].discard()
                discarded_tiles.append(last_discarded)
                print("player " + str(player_number) + " discards")
                graphics.discard_graphics(screen, discarded_tiles)
                graphics.comp_graphics(players, screen)
                # next player
                player_number = (player_number + 1) % 4
                new = True

        for event in pygame.event.get():
            # exit game
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

            if peng and new_player_number == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("clicked")
                    mouse = pygame.mouse.get_pos()
                    if event.button == 1:  # if left clicked
                        if graphics.clicked_on_discarded(mouse, discarded_tiles):
                            print("clicked on discarded")
                            player_number = new_player_number
                            players[player_number].peng(last_discarded)
                            last_discarded = discarded_tiles.pop()
                            new = False
                        else:
                            print("chose not to peng")
                            new = True
                            should_pass = True
                            graphics.clear_screen(screen)
                            graphics.comp_graphics(players, screen)
                            graphics.discard_graphics(screen, discarded_tiles)
                            tiles = gameplay.sort_tile_list(players[0].hidden_tiles)
                            graphics.player_one_graphics(
                                tiles, players[0].displayed_tiles, screen
                            )

            if player_number == 0:
                # if user clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if event.button == 1:  # if left clicked
                        pos = graphics.tile_coordinates(mouse)
                        if isinstance(
                            pos, int
                        ):  # pos only integer if clicked in tile range
                            # get tile at position
                            if pos < len(players[player_number].hidden_tiles):
                                last_discarded = gameplay.sort_tile_list(
                                    players[player_number].hidden_tiles
                                )[pos]
                                # add to list of discarded
                                discarded_tiles.append(last_discarded)
                                graphics.discard_graphics(screen, discarded_tiles)
                                # remove from user's tiles and update graphics
                                players[player_number].hidden_tiles.remove(
                                    last_discarded
                                )
                                graphics.clear_screen(screen)
                                graphics.comp_graphics(players, screen)
                                graphics.discard_graphics(screen, discarded_tiles)
                                tiles = gameplay.sort_tile_list(players[0].hidden_tiles)
                                graphics.player_one_graphics(
                                    tiles, players[0].displayed_tiles, screen
                                )
                                player_number = (player_number + 1) % 4
                                new = True
                                should_pass = False

    # run out of tiles
    if len(all_tiles) == 0:
        print("Nobody won")
