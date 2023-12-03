from aocd.models import Puzzle
from string import punctuation
import numpy as np
from functools import reduce

def retrieve_puzzle_input():
    '''Get challenge data
    Returns: Input data as a single string'''
    data = Puzzle(year=2023, day=3)
    return data.input_data

def main():
    lines = retrieve_puzzle_input().split("\n")

    NUM_LINES = len(lines)
    LINE_LEN = len(lines[0])

    # find all the instances of numbers within the schematic in the form
    # of a tuple, where the first element is the number itself and the second
    # is another tuple, a triple which contains the line the number is on, the
    # start index of the number, and the end index of the number (inclusive)
    nums = []
    for i in range(len(lines)):
        j = 0
        while j < LINE_LEN:
            if lines[i][j].isdecimal():
                start = j
                num = ""
                while j < LINE_LEN and lines[i][j].isdecimal():
                    num += lines[i][j]
                    j += 1
                j -= 1
                nums.append((int(num), (i, start, j)))

            j += 1

    # loop through every instance of a number in the schematic, checking
    # whether any of the characters around it is a symbol. if it is, add the
    # number to the sum
    gears = {}
    for num in nums:
        for i in range(num[1][0] - 1, num[1][0] + 2):
            if i >= 0 and i < NUM_LINES:
                for j in range(num[1][1] - 1, num[1][2] + 2):
                    if j >= 0 and j < LINE_LEN:
                        if lines[i][j] == "*":
                            if not gears.get((i, j)):
                                gears[(i, j)] = []
                            gears[(i, j)].append(num[0])

    gear_ratio_sum = 0
    for gear in gears:
        if len(gears[gear]) == 2:
            gear_ratio_sum += reduce(lambda a, b: a * b, gears[gear])

    print(gear_ratio_sum)


if __name__ == "__main__":
    main()

# Part 1: Replaced with code above
#
# def parse_input(data):
#     data_list = data.split("\n")
#     padded_lines = [("." + line.strip() + ".") for line in data_list]
#     character_lists = [[c for c in line] for line in padded_lines]
#     pad_row = np.full((1,len(character_lists[0])),".")
#     input_array = np.array(character_lists)
#     return np.vstack((pad_row,input_array,pad_row))

# def find_symbols(engine_array, symbol):
#     symbol_coords = []
#     for y,row in enumerate(engine_array):
#         for x,loc in enumerate(row):
#             if loc != symbol:
#                 continue
#             if loc == symbol:
#                 coords = (y,x)
#             symbol_coords.append(coords)
#     return set(symbol_coords)

# def parse_number_coordinates(engine_array):
#     number_coords = []
#     for y,row in enumerate(engine_array):
#         left = 0
#         right = 0
#         for x,loc in enumerate(row):
#             if loc == ".":
#                 continue
#             if loc.isnumeric() and not row[x-1].isnumeric():
#                 coords = (y,x)
#             number_coords.append(coords)
#     return set(number_coords)

# def create_number_windows(engine_array,coord_set):
#     window_arrays = []
#     numbers = []
#     for pair in coord_set:
#         y = pair[0]
#         left = pair[1] - 1
#         right = pair[1] + 1
#         attempt_slice = engine_array[y,left:right]
#         ends_match = not attempt_slice[0].isnumeric() and not attempt_slice[-1].isnumeric()
#         # keep searching to the right until number ends
#         while ends_match == False:
#             attempt_slice = engine_array[y,left:right]
#             ends_match = not attempt_slice[0].isnumeric() and not attempt_slice[-1].isnumeric()
#             if not ends_match:
#                 right += 1
#             if ends_match:
#                 full_number = "".join(engine_array[y,left+1:right-1])
#                 numbers.append(int(full_number))
#                 window_arrays.append(engine_array[y-1:y+2,left:right])
#     return list(zip(coord_set,numbers,window_arrays))

# def search_lines(window_list):
#     total_part_1 = 0
#     gears = {}
#     for window in window_list:
#         flat_window = window[2].ravel()
#         for i in flat_window:
#             if i == ".":
#                 continue
#             if i in punctuation:
#                 total_part_1 += window[1]
#                 break
#     return total_part_1

# test_input = '''467..114..
#                 ...*......
#                 ..35..633.
#                 ......#...
#                 617*......
#                 .....+.58.
#                 ..592.....
#                 ......755.
#                 ...$.*....
#                 .664.598..'''

# def main():
#     data = retrieve_puzzle_input()
#     array = parse_input(test_input)
#     coords = parse_number_coordinates(array)
#     window_list = create_number_windows(array,coords)
#     print(f"Part 1 solution: {search_lines(window_list)}")
#     print(window_list)

# if __name__ == "__main__":
#     print(main())
