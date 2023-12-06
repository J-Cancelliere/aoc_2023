from aocd.models import Puzzle
import regex as re

def retrieve_puzzle_data():
    puzzle = Puzzle(year=2023, day=6)
    return puzzle.input_data

def parse_puzzle_input(puzzle_input, bad_kern=False):
    input_dict = {}
    for line in puzzle_input.split("\n"):
        num_pattern = "\d{1,4}"
        key_index = line.find(" ")
        new_key = line[:key_index-1]
        numbers = re.findall(num_pattern, line)
        if bad_kern:
            numbers = "".join(numbers)
            input_dict[new_key] = int(numbers)
            continue
        input_dict[new_key] = [int(num) for num in numbers]
    if bad_kern:
        return input_dict.values()
    return input_dict

def calc_ways_to_win(race):
    # search up
    win_lower = 0
    for i in range(1,race[0]):
        time_left = race[0] - i
        distance = i * time_left
        if distance > race[1]:
            win_lower = i
            break
    # search down
    win_upper = 0
    for i in reversed(range(1,race[0])):
        time_left = race[0] - i
        distance = i * time_left
        if distance > race[1]:
            win_upper = i + 1
            break
    return win_upper - win_lower

def final_product(input_dict):
    final_product = 1
    for race in zip(input_dict["Time"],input_dict["Distance"]):
        multiplier = calc_ways_to_win(race)
        final_product *= multiplier
    return final_product

def main():
    puzzle_input = retrieve_puzzle_data()
    input_dict = parse_puzzle_input(puzzle_input)
    part_1 = final_product(input_dict)
    print(f"Answer to part 1: {part_1}")
    part_2_input = tuple(parse_puzzle_input(puzzle_input, bad_kern=True))
    part_2 = calc_ways_to_win(part_2_input)
    print(f"Answer to part 2: {part_2}")


if __name__ == "__main__":
    print(main())
