from aocd.models import Puzzle
import time

NAV_POINTS = {"|": ((-1,0), (1,0)),
          "-": ((0,-1), (0,1)),
          "F": ((1,0), (0,1)),
          "7": ((0,-1), (1,0)),
          "L": ((-1,0), (0,1)),
          "J": ((0,-1), (-1,0))}

def retrieve_puzzle_input():
    puzzle = Puzzle(year=2023, day=10)
    return puzzle.input_data

def parse_grid(puzzle_input):
    rows = puzzle_input.split("\n")
    return rows

# Find starting position, pick a direction
def find_start(grid):
    start = (0,0)
    for i,line in enumerate(grid):
        start_index = line.find("S")
        if start_index != -1:
            start = (i,start_index)
            break
    return start

# Start following loop
#   Loop navigation
#   Given previous location
#   Determine next direction
# Keep history of steps in loop
# Return to start
def follow_loop(grid,start):
    r,c = start
    history = []
    looping = True
    prev = (0,0)
    while looping:
        if history.count("S") == 2:
            looping = False
            continue
        navigation = NAV_POINTS.get(grid[r][c])
        # getting out of start position
        if not navigation:
            history.append("S")
            search_list = [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]
            for point in search_list:
                symbol = grid[point[0]][point[1]]
                if symbol in NAV_POINTS.keys():
                    for nav in NAV_POINTS[symbol]:
                        if (point[0]+nav[0],point[1]+nav[1]) == (r,c):
                            prev = (r,c)
                            r,c = point
                            break
        # every other position
        else:
            for points in navigation:
                next = (r + points[0], c + points[1])
                if next == prev:
                    continue
                else:
                    history.append(grid[r][c])
                    prev = (r,c)
                    r,c = next
                    break
    return {"steps": len(history), "history": history}

# Divide steps by 2 (halfway point)
# Return halfway point
def halfway_point(steps):
    return int(steps / 2)

def main():
    puzzle = retrieve_puzzle_input()
    grid = parse_grid(puzzle)
    start = find_start(grid)
    history = follow_loop(grid,start)
    part1 = halfway_point(history["steps"])
    return f"Answer to part 1: {part1}"

if __name__ == "__main__":
    print(main())
