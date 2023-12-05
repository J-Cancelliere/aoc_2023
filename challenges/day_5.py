from aocd.models import Puzzle
import regex as re

def retrieve_puzzle_input():
    puzzle = Puzzle(year=2023, day=5)
    return puzzle.input_data

def parse_puzzle_input(puzzle_input):
    '''Convert the puzzle input from a single string into lists
    Takes 1 arg, input string
    Returns a Tuple:
        - 1st element is list of seed numbers (int)
        - 2nd element is a dict with maps for keys and lists of
        tuples as values. Each tuple contains 2 integers for the mapping'''
    # Create a list of seed numbers
    seeds_index = puzzle_input.find("\n")
    seed_line = puzzle_input[:seeds_index].strip("seeds: ")
    seed_list = [int(seed) for seed in seed_line.split(" ")]
    puzzle_input = puzzle_input[seeds_index:]
    # Find the mapping names
    pattern = ".+?:"
    keys = re.findall(pattern,puzzle_input)
    keys = [key.strip(" map:") for key in keys]
    # Create a list of map lines for each map
    map_list = []
    next_map = puzzle_input.find(":")
    while next_map > 0:
        start = next_map + 2 # exclude colon & next newline
        puzzle_input = puzzle_input[start:]
        end_map = puzzle_input.find("\n\n")
        map = puzzle_input[:end_map]
        if end_map == -1: # Condition for last mapping in input
            map = puzzle_input
        lines = map.split("\n")
        split_lines = [line.split(" ") for line in lines]
        parsed_maps = [tuple([int(num) for num in map]) for map in split_lines]
        map_list.append(parsed_maps)
        next_map = puzzle_input.find(":")
    # TODO: Combine keys and map_list into a singe dict.
    map_dict = dict(zip(keys,map_list))
    return (seed_list,map_dict)

# Tried making a dict - input data was way too big.
# def make_mappings(map_dict):
#     '''Create a new dictionary for all the almanac mappings
#     Returns a dict:
#         - keys are the mapping destination
#         - values are a dict containing mapping from source values
#         to destination values'''
#     map_keys = map_dict.keys()
#     for key in map_keys:
#         print(f"Values for {key}:")
#         for i,line in enumerate(map_dict[key]):
#             print(f"\nCompiling mapping {i+1}:")
#             destination = line[0]
#             source = line[1]
#             range_len = line[2]
#             print(f"\tSource start = {source}")
#             print(f"\tDestination start = {destination}")
#             print(f"\tRange = {range_len}")
#             source_list = range(source,source+range_len)
#             destination_list = range(destination,destination+range_len)
#         break


def convert_number(source_number,mapping):
    '''generate an updated number based on the mapping provided
    source_number is a singe int. mapping is the 3-tuple containing the source,
    destination, and range of the mappings'''
    destination = mapping[0]
    source = mapping[1]
    range_len = mapping[2]
    if source_number < source:
        return source_number
    if source_number >= source:
        source_diff = source_number - source
        if source_diff <= range_len:
            return source_diff + destination
        else:
            return source_number

def catalogue_seed_data(seed_list, map_dict):
    '''Creates a dict for each seed by searching all mappings
    - Key is the seed ID
    - Value is a tuple containing the 7 growing values'''
    seed_dict = {}
    for seed in seed_list:
        print(f"\nCataloguing seed ID {seed}")
        running_num = seed
        grow_vals = []
        for key in map_dict.keys():
            map_list = map_dict[key]
            for map in map_list:
                new_num = convert_number(running_num,map)
                if new_num != running_num:
                    grow_vals.append(new_num)
                    running_num = new_num
                    print(f"\t{key} value is {running_num}")
                    break
                if map == map_list[-1]:
                    grow_vals.append(new_num)
                    print(f"\t{key} value is {running_num}")
        seed_dict[seed] = grow_vals
    return seed_dict

def get_lowest_loc(seed_catalogue):
    lowest_value = 0
    for seed in seed_catalogue.keys():
        if lowest_value == 0:
            lowest_value = seed_catalogue[seed][-1]
        if lowest_value > seed_catalogue[seed][-1]:
            lowest_value = seed_catalogue[seed][-1]
    return lowest_value

def main():
    puzzle_input = retrieve_puzzle_input()
    seeds, maps = parse_puzzle_input(puzzle_input)
    seed_catalogue = catalogue_seed_data(seeds,maps)
    return get_lowest_loc(seed_catalogue)

if __name__ == "__main__":
    print(main())
