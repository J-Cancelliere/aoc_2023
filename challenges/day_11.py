from aocd.models import Puzzle

def retrieve_puzzle_input():
    puzzle = Puzzle(year=2023, day=11)
    return puzzle.input_data

def expand_rows(puzzle_input):
    lines = puzzle_input.split("\n")
    width = len(lines[0])
    empty_indices = []
    for i,line in enumerate(lines):
        if line.count(".") == width:
            empty_indices.append(i)
    for idx in empty_indices:
        lines.insert(idx,lines[i])
    return lines

def expand_columns(lines):
    width = len(lines[0])
    empty_indices = []
    for i in range(0,width):
        stop = -1
        for j,line in enumerate(lines):
            if line[i] != ".":
                stop = j
                break
            elif j == (len(line)-1):
                empty_indices.append(i)
        if stop > -1:
            continue
    new_lines = []
    for line in lines:
        new_line = line
        for idx in reversed(empty_indices):
            new_line = new_line[:idx] + new_line[idx] + new_line[idx:]
        new_lines.append(new_line)
    return new_lines

def count_paths():
    # for each galaxy (#)
    #   start search to the right, the down 1 and left, then right, and so on
    #   record each step
    #   if you encounter a galaxy, check if it's already matched
    #       if yes, continue along the search path
    #       if no, record number of steps, galaxy coordinates, continue search
    pass

def main():
    puzzle = retrieve_puzzle_input()
    rows = expand_rows(puzzle)
    expanded_universe = expand_columns(rows)
    return expanded_universe

if __name__ == "__main__":
    print(main())
