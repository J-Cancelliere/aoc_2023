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
    result = day_8.calculate_steps(result1,result2,"AAA","ZZZ")
    assert result == 6

# part 2 tests
test2_input = """LR

AAA = (BBB, XXX)
BBB = (XXX, ZZZ)
ZZZ = (BBB, XXX)
ABA = (BCB, XXX)
BCB = (CDC, CDC)
CDC = (ZXZ, ZXZ)
ZXZ = (BCB, BCB)
XXX = (XXX, XXX)"""

def test_part2_parsing():
    # given the test2 input
    # when parsing the data
    # return "LR", dict{"AAA": ("BBB","BBB"), ...}, and two lists:
    # [all locs ending "A"], [all locs ending "Z"]
    result1, result2, result3 = day_8.parse_puzzle_input_2(test2_input)
    assert result1 == "LR"
    assert result2["AAA"] == ("BBB","XXX")
    assert result2["ZZZ"] == ("BBB","XXX")
    assert result3[0] == ["AAA", "ABA"]
    assert result3[1] == ["ZZZ", "ZXZ"]

def test_calculation_2():
    # given the test2 input
    # when counting steps
    # return 6
    result1, result2, result3 = day_8.parse_puzzle_input_2(test2_input)
    result = day_8.calculate_steps_2(result1,result2,result3)
    assert result == 6
