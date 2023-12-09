from challenges import day_9

test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

# part 1 tests

def test_next_value():
    # Given the test input above
    # When predicting the next number in the sequence
    # return 18, 28, 68
    parsed_test = day_9.parse_input(test_input)
    result1 = day_9.next_number(parsed_test[0])
    result2 = day_9.next_number(parsed_test[1])
    result3 = day_9.next_number(parsed_test[2])
    assert result1 == 18
    assert result2 == 28
    assert result3 == 68
