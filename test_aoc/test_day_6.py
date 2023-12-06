from challenges import day_6

test_input="""Time:      7  15   30
Distance:  9  40  200"""

def test_individual_race():
    # given the inputs (7, 9), (15,40), (30, 200)
    # when calculating ways to win
    # return 4, 8, 9
    result1 = day_6.calc_ways_to_win((7,9))
    assert result1 == 4
    result2 = day_6.calc_ways_to_win((15,40))
    assert result2 == 8
    result3 = day_6.calc_ways_to_win((30,200))
    assert result3 == 9

def test_final_product():
    # given the parsed test input (above)
    # when calculating the final product
    # return 288
    test_parsed = day_6.parse_puzzle_input(test_input)
    result = day_6.final_product(test_parsed)
    assert result == 288
