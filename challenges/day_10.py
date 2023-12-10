from aocd.models import Puzzle

def retrieve_puzzle_input():
    puzzle = Puzzle(year=2023, day=10)
    return puzzle.input_data

def parse_grid():
    pass

# Find starting position, pick a direction
def find_start():
    pass


# Start following loop
#   Loop navigation
#   Given previous location
#   Determine next direction
# Keep history of steps in loop
# Return to start
def follow_loop():
    pass

# Divide steps by 2 (halfway point)
# Return halfway point
def halfway_point():
    pass

def main():
    pass

if __name__ == "__main__":
    print(main())
