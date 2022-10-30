
import random

class Tile:
    def __init__(self, suit_type, value):
        self.suit_type = suit_type
        self.value = value

    def __eq__(self, other):
        return (self.suit_type == other.suit_type) and (self.value == other.value)

suit_values = {
    "Numbers": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "Circles": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "Bamboo": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
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
            if test_list.count(tile) < 3 and (
                tile.suit_type in ["Numbers", "Bamboo", "Circles"]
            ):
                tile2 = Tile(tile.suit_type, str(int(tile.value) + 1))
                tile3 = Tile(tile.suit_type, str(int(tile.value) + 2))
                if tile2 in test_list and tile3 in test_list:
                    test_list.remove(tile)
                    test_list.remove(tile2)
                    test_list.remove(tile3)
                else:
                    break
            elif test_list.count(tile) < 3:
                break
            else:  # because sorted so if appears more than twice has to be part of triplet?
                test_list.remove(tile)
                test_list.remove(tile)
                test_list.remove(tile)
        if len(test_list) == 0:  # if while loop terminated naturally then valid win
            return True

    return False


def check_for_win_old(tile_list):
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

def check_for_sets_of_three(test_list):

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
                return False
        else:
            # because sorted so if appears more than twice has to be part of triplet?
            try:
                test_list.remove(tile)
                test_list.remove(tile)
                test_list.remove(tile)
            except:
                return False
    return True



def check_for_win_edited(tile_list):

    possible_pairs = []
    for tile in tile_list:
        if tile_list.count(tile) >= 2:
            possible_pairs.append(tile)

    for pair in possible_pairs:
        test_list = tile_list.copy()
        test_list.remove(pair)
        test_list.remove(pair)
        if check_for_sets_of_three(test_list):
            return True
    return False

# and isinstance(tile.value, int)
# special_case = [Tile("Circles", "1"),Tile("Circles", "1"),Tile("Circles", "1"),\
#             Tile("Circles", "2"),Tile("Circles", "3"),Tile("Circles", "4"),\
#                 Tile("Circles", "6"),Tile("Circles", "7"),Tile("Circles", "8"),\
#                     Tile("Dragon", "Z"),Tile("Dragon", "Z"),\
#                         Tile("Wind", "N"),Tile("Wind", "N"),Tile("Wind", "N")]
special_case = [Tile("Bamboo", "1"),Tile("Bamboo", "2"),Tile("Bamboo", "3"),\
            Tile("Bamboo", "1"),Tile("Bamboo", "2"),Tile("Bamboo", "3"),\
                Tile("Circles", "6"),Tile("Circles", "7"),Tile("Circles", "8"),\
                    Tile("Dragon", "Z"),Tile("Dragon", "Z"),\
                        Tile("Bamboo", "3"),Tile("Bamboo", "4"),Tile("Bamboo", "5")]
print_tiles(special_case)
print(check_for_win(special_case))
try:
    check = False
    while check == False:
        
        all_tiles = create_tiles()
        test_case = []
        # for i in range(15):
        for j in range(14):
            index = random.randint(0,len(all_tiles)-1)
            test_case.append(all_tiles[index])
            del all_tiles[index]
        test_case = sort_tile_list(test_case)
            # test_case.append([])
        # del test_case[-1]
        if check_for_win(test_case):
            print_tiles(test_case)
            print(check_for_win(test_case))
        
except Exception as e:
    print(e)

