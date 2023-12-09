from aocd.models import Puzzle
import time
import math

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
    steps, nodes_dict = parse_puzzle_input(puzzle_input)
    a_list = []
    z_list = []
    for key in nodes_dict.keys():
        if key[-1] == "A":
            a_list.append(key)
        if key[-1] == "Z":
            z_list.append(key)
    return steps, nodes_dict, (a_list,z_list)

def calculate_steps(steps,node_dict,start,finish):
    current_loc = start
    step_limit = len(steps)
    total_steps = 0
    timeout = time.time() + 1
    while True:
        if current_loc == finish:
            break
        step = 0
        if time.time() > timeout:
            return None
        while step < step_limit:
            if steps[step] == 'L':
                current_loc = node_dict[current_loc][0]
            else:
                current_loc = node_dict[current_loc][1]
            step += 1
            total_steps += 1
            if current_loc == finish:
                break
    return total_steps

def calculate_steps_2(steps,node_dict,az_lists):
    a_list = az_lists[0]
    z_list = az_lists[1]
    step_counts = []
    for a in a_list:
        for z in z_list:
            print(f"Checking path for {a} and {z}...")
            step_count = calculate_steps(steps,node_dict,a,z)
            if step_count:
                print(f"\tPath found: {step_count} steps")
                step_counts.append(step_count)
                break
            else:
                print(f"\tNo path between {a} and {z}")
    lcm = step_counts[0]
    for c in step_counts:
        if c == lcm:
            continue
        lcm = math.lcm(lcm,c)
    return lcm


def main():
    puzzle_data = retrieve_puzzle_input()
    steps, nodes, multi_list = parse_puzzle_input_2(puzzle_data)
    part1 = calculate_steps(steps, nodes, "AAA", "ZZZ")
    part2 = calculate_steps_2(steps,nodes,multi_list)
    return f"Answer to part 1: {part1}\nAnswer to part 2: {part2}"

if __name__ == '__main__':
    print(main())
