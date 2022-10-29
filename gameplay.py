# imports
import random
from collections import Counter

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


# Tile class definition
class Tile:
    def __init__(self, suit_type, value):
        self.suit_type = suit_type
        self.value = value

    def __eq__(self, other):
        return (self.suit_type == other.suit_type) and (self.value == other.value)


# ignored flowers for now
def create_tiles():
    all_tiles = []
    # for every suit
    for key in suit_values.keys():
        # for every value
        for value in suit_values[key]:
            # create 4 tiles
            for i in range(4):
                all_tiles.append(Tile(key, value))

    # add flowers
    # # for key in flowers.keys():
    # #     for value in flowers[key]:
    # #         all_tiles.append(Tile(key, value))

    # shuffle tiles
    random.shuffle(all_tiles)
    # return list of tiles
    return all_tiles


def print_tiles(tile_list):
    to_print = []
    # sort tiles
    tile_list = sort_tile_list(tile_list)
    # print tiles
    for tile in tile_list:
        to_print.append(tile.suit_type + tile.value)
    print(to_print)


def sort_tile_list(tile_list):
    return sorted(tile_list, key=lambda x: (x.suit_type, x.value), reverse=False)


def tile_lists_equal(tiles1, tiles2):
    tiles1 = sort_tile_list(tiles1)
    tiles2 = sort_tile_list(tiles2)
    return tiles1 == tiles2


class Player:
    def __init__(self, position, hidden_tiles, displayed_tiles):
        self.position = position
        self.hidden_tiles = hidden_tiles
        self.displayed_tiles = displayed_tiles
        # self.ignored_tiles = ignored_tiles

    def print_player_tiles(self):
        tiles = self.hidden_tiles + self.displayed_tiles
        print_tiles(tiles)

    def discard(self):
        print("Please select tile to discard:")
        tile_to_discard = float("NaN")
        while tile_to_discard not in self.hidden_tiles:
            suit = input("Enter suit (Bamboo, Circles, Numbers, Dragon or Wind):")
            value = input("Enter value:")
            tile_to_discard = Tile(suit, value)
        self.hidden_tiles.remove_tile(tile_to_discard)
        return tile_to_discard

    def chi(self, tile):
        done = False
        while not done:
            suit = tile.suit
            tile1_value = input("enter tile 1 value: ")
            tile2_value = input("enter tile 2 value: ")
            if (
                Tile(suit, tile1_value) in self.hidden_tiles
                and Tile(suit, tile2_value) in self.hidden_tiles
            ):
                # TODO: insert check that is a valid sequence
                self.hidden_tiles.remove(Tile(suit, tile1_value))
                self.hidden_tiles.remove(Tile(suit, tile2_value))
                self.displayed_tiles.append(
                    sort_tile_list(
                        [tile, Tile(suit, tile1_value), Tile(suit, tile2_value)]
                    )
                )
                done = True
            else:
                print("Invalid chi")

    def peng(self, tile):
        # TODO: insert check that tile appears at least twice in hidden tiles
        for i in range(2):
            self.hidden_tiles.remove(tile)
        self.displayed_tiles.append([tile, tile, tile])

    # ignore gong for now
    def gong(self, tile):
        # TODO: insert check that tile appears thrice in hidden tiles
        for i in range(3):
            self.hidden_tiles.remove(tile)
        self.displayed_tiles.append([tile, tile, tile, tile])

    def win(self, tile):
        # TODO
        return False


def game_setup(all_tiles):
    # distribute tiles
    players = []
    player_tiles = [[], [], [], []]
    for i in range(3):
        for j in range(4):
            for k in range(4):
                player_tiles[j].append(all_tiles[j * 4 + k])
        all_tiles = all_tiles[16:]
    for i in range(4):
        player_tiles[i].append(all_tiles[i])
    all_tiles = all_tiles[4:]
    # set up players
    for i in range(4):
        tiles = player_tiles[i]
        sort_tile_list(tiles)
        players.append(Player(i, tiles, []))
    return players, all_tiles


def pickup_tile(all_tiles):
    return all_tiles.pop(0)


def check_for_win(discarded_tile):
    if discarded_tile != discarded_tile:
        return False
    for player in players:
        print("--------- Player " + str(players.index(player)) + " ---------")
        if player.win(discarded_tile):
            print("Player " + str(players.index(player)) + " has won!")
            return True
        else:
            print("Not won yet")


def check_for_chi(player_tiles, discarded_tile):
    if discarded_tile != discarded_tile:
        return False
    if discarded_tile.suit_type != "Wind" and discarded_tile.suit_type != "Dragon":
        wanted_tiles = []
        for i in range(5):
            wanted_tiles.append(
                Tile(discarded_tile.suit_type, str(int(discarded_tile.value) - 2 + i))
            )
        new_tile_set = player_tiles.copy()
        new_tile_set.append(discarded_tile)
        for i in range(3):
            if (
                (wanted_tiles[i] in new_tile_set)
                and (wanted_tiles[i + 1] in new_tile_set)
                and (wanted_tiles[i + 2] in new_tile_set)
            ):
                return True
        # return False
    return False


def check_for_peng(discarded_tile):
    if discarded_tile != discarded_tile:
        return False, float("NaN")
    for player in players:
        if player.hidden_tiles.count(discarded_tile) >= 2:
            print("Player " + str(players.index(player)) + " PENG")
            return True, players.index(player)
    return False, float("NaN")


# have ignored gong to begin with
def check_for_gong(discarded_tile):
    # TODO
    return False


# set initial values

round = 0
prevailing = "E"
player_number = 0  # change this to player who's position is east
all_tiles = create_tiles()
players, all_tiles = game_setup(all_tiles)
discarded_tiles = []
last_discarded = float("NaN")


# gameplay for single round

while not check_for_win(last_discarded) and round < 1:
    # only for checking stuff
    round = 1

    print(players)
    for player in players:
        print(player.position)
        player.print_player_tiles()

    peng, new_player_number = check_for_peng(last_discarded)
    if peng:
        player_number = new_player_number
        players[player_number].peng(last_discarded)
        last_discarded = players[player_number].discard()

    chi = check_for_chi(players[player_number], last_discarded)
    if not peng and chi:
        players[player_number].chi(last_discarded)
        last_discarded = players[player_number].discard()

    if not peng and not chi and last_discarded != float("NaN"):
        discarded_tiles.append(last_discarded)
        print("Player" + str(player_number))
        players[player_number].hidden_tiles.append(pickup_tile(all_tiles))
        players[player_number].print_player_tiles()
