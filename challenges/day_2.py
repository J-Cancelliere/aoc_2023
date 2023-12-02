from aocd.models import Puzzle

LIMITS = {"red": 12,
          "green": 13,
          "blue": 14}

def retrieve_challenge_input():
    data = Puzzle(year=2023, day=2)
    return data.input_data

def parse_data_part_1(data):
    data_list = data.split('\n')
    data_dict = {}
    for line in data_list:
        # Find colon index and split game from rest of string
        key_split = line.find(':')
        new_key = line[:key_split]
        attempts = line[key_split + 1:]
        # Parse rest of line into list of tuples
        attempts = attempts.replace(';',',')
        attempt_list = attempts.split(',')
        split_vals = [tuple(attempt.strip().split(' ')) for attempt in attempt_list]
        new_val = []
        for pair in split_vals:
            number = int(pair[0])
            color = pair[1]
            new_val.append((number,color))
        data_dict[new_key] = new_val
    return data_dict

def verify_game_part_1(game_list):
    for game in game_list:
        if game[0] > LIMITS[game[1]]:
            return False
    return True

def convert_keys_to_int(data_dict):
    new_dict = {}
    for game in data_dict.keys():
        new_key = int(game.strip('Game '))
        new_dict[new_key] = data_dict[game]
    return new_dict

def find_min_values(game_list):
    minimum_cubes = {}
    for game in game_list:
        if not minimum_cubes.get(game[1]):
            minimum_cubes[game[1]] = game[0]
        elif minimum_cubes.get(game[1]) > game[0]:
            continue
        else:
            minimum_cubes[game[1]] = game[0]
    return minimum_cubes

def multiply_cubes(part_2_mins):
    numbers = list(part_2_mins.values())
    return numbers[0] * numbers[1] * numbers[2]

def main():
    data = retrieve_challenge_input()
    data_dict = parse_data_part_1(data)
    number_dict = convert_keys_to_int(data_dict)
    results = [verify_game_part_1(game) for game in number_dict.values()]
    results_dict = dict(zip(number_dict.keys(),results))
    total_part1 = 0
    for k in results_dict.keys():
        if results_dict[k] == True:
            total_part1 += k
    print(f"Part 1 answer: {total_part1}")
    part_2_mins = [find_min_values(game) for game in data_dict.values()]
    part_2_products = [multiply_cubes(cubes) for cubes in part_2_mins]
    total_part2 = sum(part_2_products)
    print(f"Part 2 answer: {total_part2}")


if __name__ == '__main__':
    main()
