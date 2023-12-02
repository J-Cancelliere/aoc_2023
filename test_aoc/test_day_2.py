from challenges import day_2

test_data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

# Part 1 tests
def test_parse_part_1():
    '''Given the test data provided
    When parsing all games
    Return a dict where keys are the game and values are a list of tuples'''
    result = day_2.parse_data_part_1(test_data)
    assert result["Game 1"] == [(3,"blue"),(4,"red"),(1,"red"),(2,"green"),(6,"blue"),(2,"green")]

def test_successful_game():
    '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    When verifying this game
    Then the function returns True'''
    result = day_2.verify_game_part_1()
    assert result == True

def test_failed_game():
    '''Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    When verifying this game
    Then the function returns False'''
    result = day_2.verify_game_part_1()
    assert result == False
