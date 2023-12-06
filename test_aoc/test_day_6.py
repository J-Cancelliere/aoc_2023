from challenges import day_6

test_input="""Time:      7  15   30
Distance:  9  40  200"""

test_parsed = day_6.parse_puzzle_input(test_input)

def test_individual_race():
    # given the inputs 7, 9
    # when calculating ways to win
    # return 4
    result = day_6.calc_ways_to_win((7,9))
    assert result == 4

def test_final_product():
    # given the parsed test input (above)
    # when calculating the final product
    # return 288
    result = day_6.final_product(test_parsed)
    assert result == 288
