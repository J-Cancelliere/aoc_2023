from challenges import day_8

test_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

# part 1 tests

def test_parsing():
    # given the test input
    # when parsing the data
    # return "LLR" and dict{"AAA": ("BBB","BBB"), ...}
    result1, result2 = day_8.parse_puzzle_input(test_input)
    assert result1 == "LLR"
    assert result2["AAA"] == ("BBB","BBB")
    assert result2["ZZZ"] == ("ZZZ","ZZZ")

def test_calculation():
    # given the test input
    # when counting steps
    # return 6
    result1, result2 = day_8.parse_puzzle_input(test_input)
    result = day_8.calculate_steps(result1,result2)
    assert result == 6
