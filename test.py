from math import fabs
import random

class Tile:
    def __init__(self, suit_type, value):
        self.suit_type = suit_type
        self.value = value

    def __eq__(self, other):
        return (self.suit_type == other.suit_type) and (self.value == other.value)

suit_values = {
    "Numbers": [1,2,3,4,5,6,7,8,9],
    "Circles": [1,2,3,4,5,6,7,8,9],
    "Bamboo": [1,2,3,4,5,6,7,8,9],
    "Wind": ["E", "S", "W", "N"],
    "Dragon": ["B", "Z", "F"],
}

def sort_tile_list(tile_list):
    return sorted(tile_list, key=lambda x: (x.suit_type, x.value), reverse=False)

def print_tiles(tile_list):
    to_print = []
    # sort tiles
    tile_list = sort_tile_list(tile_list)
    # print tiles
    for tile in tile_list:
        to_print.append(tile.suit_type + str(tile.value))
    print(to_print)

def create_tiles():
    all_tiles = []
    # for every suit
    for key in suit_values.keys():
        # for every value
        for value in suit_values[key]:
            # create 4 tiles
            for i in range(4):
                all_tiles.append(Tile(key, value))
        all_tiles.append(Tile(key, value))

    # random.shuffle(all_tiles)
    # return list of tiles
    return all_tiles
def check_for_win(tile_list):

    tile_set = []
    for tile in tile_list:
        if tile not in tile_set:
            tile_set.append(tile)

    possible_pairs = []
    for tile in tile_set:
        if tile_list.count(tile) >= 2:
            possible_pairs.append(tile)

    for pair in possible_pairs:
        test_list = tile_list.copy()
        test_list.remove(pair)
        test_list.remove(pair)
        # remaining is either part of sequence or part of triplet
        while len(test_list) > 0:
            tile = test_list[0]
            if test_list.count(tile) < 3:
                if isinstance(tile.value, str):
                    return
                tile2 = Tile(tile.suit_type, str(int(tile.value) + 1))
                tile3 = Tile(tile.suit_type, str(int(tile.value) + 2))
                if tile2 in test_list and tile3 in test_list:
                    test_list.remove(tile)
                    test_list.remove(tile2)
                    test_list.remove(tile3)
                else:
                    return False
            else:  # because sorted so if appears more than twice has to be part of triplet?
                test_list.remove(tile)
                test_list.remove(tile)
                test_list.remove(tile)
        return True

    return False

def check_for_win_edited(tile_list):
    tile_set =[]
    for tile in tile_list:
            if tile not in tile_set:
                tile_set.append(tile)

    possible_pairs = []
    for tile in tile_set:
        if tile_list.count(tile) >= 2:
            possible_pairs.append(tile)

    for pair in possible_pairs:
        test_list = tile_list.copy()
        test_list.remove(pair)
        test_list.remove(pair)
        # remaining is either part of sequence or part of triplet
        while len(test_list) > 0:
            tile = test_list[0]
            if test_list.count(tile) < 3 and isinstance(tile.value, int):
                tile2 = Tile(tile.suit_type, (tile.value) + 1)
                tile3 = Tile(tile.suit_type, (tile.value) + 2)
                if tile2 in test_list and tile3 in test_list:
                    test_list.remove(tile)
                    test_list.remove(tile2)
                    test_list.remove(tile3)
                else:
                    return 
            elif isinstance(tile.value, str):
                if tile not in possible_pairs:
                    return False
                else:
                    break
            else:
                # because sorted so if appears more than twice has to be part of triplet?
                test_list.remove(tile)
                test_list.remove(tile)
                test_list.remove(tile)
            return True

    return False
# and isinstance(tile.value, int)
try:
    check = False
    while check == False:
        # special_case = [Tile("Circles", 1),Tile("Circles", 1),Tile("Circles", 1),\
        #     Tile("Circles", 2),Tile("Circles", 3),Tile("Circles", 4),\
        #         Tile("Circles", 6),Tile("Circles", 7),Tile("Circles", 8),\
        #             Tile("Dragon", "Z"),Tile("Dragon", "Z"),\
        #                 Tile("Wind", "N"),Tile("Wind", "N"),Tile("Wind", "N")]
        # print_tiles(special_case)
        # print(check_for_win(special_case))
        all_tiles = create_tiles()
        test_cases = [[]]
        for i in range(10):
            for j in range(8):
                index = random.randint(0,len(all_tiles)-1)
                test_cases[i].append(all_tiles[index])
                del all_tiles[index]
            test_cases[i] = sort_tile_list(test_cases[i])
            test_cases.append([])

        del test_cases[-1]
        for case in test_cases: 
            if check_for_win(case):
                print_tiles(case)
                print(check_for_win(case))
        
except Exception as e:
    print(e)

