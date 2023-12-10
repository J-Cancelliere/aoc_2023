from challenges import day_10

test_input_1 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

test_input_2 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

# part 1 tests

def test_starting_position():
    # given test inputs 1 and 2
    # when searching for the starting position
    # return coordinates 0,1 and 1,0 respectively
    grid1 = day_10.parse_grid(test_input_1)
    grid2 = day_10.parse_grid(test_input_2)
    result1 = day_10.find_start(grid1)
    result2 = day_10.find_start(grid2)
    assert result1[0] == 0
    assert result1[1] == 1
    assert result2[0] == 1
    assert result2[1] == 0

def test_history_start_finish():
    # given test inputs 1 and 2
    # when following the loops
    # returned history should always start and end with "S"
    grid1 = day_10.parse_grid(test_input_1)
    grid2 = day_10.parse_grid(test_input_2)
    start1 = day_10.find_start(grid1)
    start2 = day_10.find_start(grid2)
    result1 = day_10.follow_loop(start1)
    result2 = day_10.follow_loop(start2)
    assert result1["history"][0] == "S"
    assert result1["history"][-1] == "S"
    assert result2["history"][0] == "S"
    assert result2["history"][-1] == "S"

def test_step_counter():
    # given test inputs 1 and 2
    # when following the loops
    # returned step counts should 8 and 16 respectively
    grid1 = day_10.parse_grid(test_input_1)
    grid2 = day_10.parse_grid(test_input_2)
    start1 = day_10.find_start(grid1)
    start2 = day_10.find_start(grid2)
    result1 = day_10.follow_loop(start1)
    result2 = day_10.follow_loop(start2)
    assert result1["steps"][0] == 8
    assert result2["steps"][0] == 16

def test_halfway_value():
    # given test inputs 1 and 2
    # when calculating the halfway point
    # return 4 and 8 respectively
    grid1 = day_10.parse_grid(test_input_1)
    grid2 = day_10.parse_grid(test_input_2)
    start1 = day_10.find_start(grid1)
    start2 = day_10.find_start(grid2)
    history1 = day_10.follow_loop(start1)
    history2 = day_10.follow_loop(start2)
    result1 = day_10.halfway_point(history1["steps"])
    result2 = day_10.halfway_point(history2["steps"])
    assert result1 == 4
    assert result2 == 8
