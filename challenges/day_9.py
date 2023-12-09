from aocd.models import Puzzle
import time

def retreive_puzzle_input():
    puzzle = Puzzle(year=2023, day=9)
    return puzzle.input_data

def parse_input(puzzle_input):
    lines = []
    for line in puzzle_input.split("\n"):
        lines.append([int(n) for n in line.split(" ")])
    return lines

def next_number(sequence):
    history = [sequence]
    # Loop through diffs
    loop_condition = [True]
    while sum(loop_condition) != 0:
        s_len = len(sequence)
        i = 1
        next_s = []
        loop_condition = []
        while i < s_len:
            val = sequence[i] - sequence[i-1]
            next_s.append(val)
            if val != 0:
                loop_condition.append(True)
            i += 1
        sequence = next_s
        history.append(sequence)
    history = [h + [0] for h in history]
    h_len = len(history) * -1
    i = -2
    # add next in sequence
    while i >= h_len:
        prev = i + 1
        step = history[i]
        below = history[prev]
        step[-1] = step[-1] + step[-2] + below[-1]
        i -= 1
    return history[0][-1]

def main():
    puzzle = retreive_puzzle_input()
    parsed = parse_input(puzzle)
    next_in_sequence = [next_number(sequence) for sequence in parsed]
    return sum(next_in_sequence)

if __name__ == "__main__":
    print(main())
