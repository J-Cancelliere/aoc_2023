from challenges import day_4

test_data = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

one_card_many = ([41, 48, 83, 86, 17],[83, 86, 6, 31, 17, 9, 48, 53],0)
one_card_one = ([41, 48, 83, 86, 17],[83, 89, 6, 31, 10, 9, 99, 53],0)
one_card_none = ([41, 48, 83, 86, 17],[80, 84, 6, 31, 14, 9, 44, 54],0)

# part 1 tests
def test_no_match():
    #  When checking value of one_card_none
    # Then return 0
    result = day_4.get_point_value(one_card_none)
    assert result[2] == 0

def test_one_match():
    #  When checking value of one_card_one
    # Then return 1
    result = day_4.get_point_value(one_card_one)
    assert result[2] == 1

def test_many_match():
    #  When checking value of one_card_many
    # Then return 8
    result = day_4.get_point_value(one_card_many)
    assert result[2] == 8

def test_input_cleaning():
    # When sorting the input strings
    # The winning numbers should always be shorter than the card numbers
    result = day_4.process_input(test_data)
    assert len(result["Card 1"][0]) < len(result["Card 1"][1])
