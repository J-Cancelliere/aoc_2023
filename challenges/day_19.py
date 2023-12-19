from aocd.models import Puzzle

def retrieve_puzzle_input():
    puzzle = Puzzle(year=2023, day=19)
    data = puzzle.input_data.split("\n\n")
    return data[0],data[1]

def parse_workflows(input_data):
    pass

def parse_part_lists(input_data):
    pass

def accept_or_reject(workflows,part):
    pass

def p1_final_sum(accepted_list):
    pass

def main():
    pass

if __name__ == "__main__":
    print(main())
