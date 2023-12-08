from aocd.models import Puzzle

def retrieve_puzzle_input():
    puzzle = Puzzle(year=2023, day=8)
    return puzzle.input_data

def parse_puzzle_input(puzzle_input):
    steps_split = puzzle_input.find('\n')
    steps = puzzle_input[:steps_split]
    puzzle_input = puzzle_input[steps_split+2:]
    lines = puzzle_input.split('\n')
    nodes_dict = {}
    for line in lines:
        key_vals = line.split('=')
        key = key_vals[0].strip()
        value = key_vals[1].strip()
        value = value[1:len(value)-1]
        value = tuple([v.strip() for v in value.split(',')])
        nodes_dict[key] = value
    return steps,nodes_dict

def parse_puzzle_input_2(puzzle_input):
    pass

def calculate_steps(steps,node_dict):
    current_loc = 'AAA'
    step_limit = len(steps)
    total_steps = 0
    while True:
        if current_loc == "ZZZ":
            break
        step = 0
        while step < step_limit:
            if steps[step] == 'L':
                current_loc = node_dict[current_loc][0]
            else:
                current_loc = node_dict[current_loc][1]
            step += 1
            total_steps += 1
            if current_loc == "ZZZ":
                break
    return total_steps

def calculate_steps_2(steps,node_dict,az_lists):
    pass

def main():
    puzzle_data = retrieve_puzzle_input()
    steps, nodes = parse_puzzle_input(puzzle_data)
    part1 = calculate_steps(steps, nodes)
    return f"Answer to part 1: {part1}\nAnswer to part 2:"

if __name__ == '__main__':
    print(main())
