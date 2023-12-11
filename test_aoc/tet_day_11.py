from challenges import day_11

test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def test_row_expansion():
    # Given the test input
    # When expanding the universe
    # Return a list of 12 lines
    result = day_11.expand_rows(test_input)
    assert len(result) == 12

def test_column_expansion():
    # Given the test input
    # When expanding the universe
    # Return lines 13 characters long
    rows = day_11.expand_rows(test_input)
    result = day_11.expand_columns(rows)
    assert len(result[0]) == 13

def test_distance_measurement():
    # Given the test input
    # When expanding the universe
    # Return lines 13 characters long
    rows = day_11.expand_rows(test_input)
    expanded = day_11.expand_columns(rows)
    result = day_11.count_paths(expanded)
    assert result == 374
