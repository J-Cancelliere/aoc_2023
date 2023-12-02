from challenges import day_2

test_data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

# Part 1 tests
def test_parse_part_1():
    '''Given the test data provided
    When parsing all games
    Return a dict where keys are the game and values are a list of tuples'''
    result = day_2.parse_data_part_1(test_data)
    assert result["Game 1"] == [(3,"blue"),(4,"red"),(1,"red"),(2,"green"),(6,"blue"),(2,"green")]

successful_list = [(3,"blue"),(4,"red"),(1,"red"),(2,"green"),(6,"blue"),(2,"green")]

def test_successful_game():
    '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    When verifying this game
    Then the function returns True'''
    result = day_2.verify_game_part_1(successful_list)
    assert result == True

failed_list = [(8,'green'),(6,'blue'),(20,'red'),(5,'blue'),(4,'red'),(13,'green'),(5,'green'),(1,'red')]

def test_failed_game():
    '''Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    When verifying this game
    Then the function returns False'''
    result = day_2.verify_game_part_1(failed_list)
    assert result == False

# Part 2 tests
def test_minimum_id():
    '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    When searching for the min values
    return a dict: {"blue": 6, "red": 4, "green": 2}'''
    result = day_2.find_min_values(successful_list)
    assert result["blue"] == 6
    assert result["red"] == 4
    assert result["green"] == 2

def test_multiplier():
    '''Given an input of 6 blue, 4 red, and 2 green
    When multiplying all three numbers
    Return 48'''
    result = day_2.multiply_cubes({"blue": 6, "red": 4, "green": 2})
    assert result == 48
