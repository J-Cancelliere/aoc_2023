from challenges import day_1

# Tests for part 1
def test_extract_two_digits():
    '''Given a string ab2hrf8lk
    When extracting the value
    Then the function returns 28'''
    result = day_1.extract_calibration_values("ab2hrf8lk")
    assert result == 28

def test_extract_one_digit():
    '''Given a string kaju6ksu
    When extracting the value
    Then the function returns 66'''
    result = day_1.extract_calibration_values("kaju6ksu")
    assert result == 66

def test_extract_many_digits():
    '''Given a string jdu1fank9hfg8adh7yeh
    When extracting the value
    Then the function returns 17'''
    result = day_1.extract_calibration_values("jdu1fank9hfg8adh7yeh")
    assert result == 17

def test_extract_only_numeric_values():
    '''Given a string 56324
    When extracting the value
    Then the function returns 54'''
    result = day_1.extract_calibration_values("56324")
    assert result == 54

def test_sum_function():
    '''Given a list of numbers, [1,2,3,4,5]
    When added them together
    Then they return 15 '''
    result = day_1.sum_calibration_values([1,2,3,4,5])
    assert result == 15

# Tests for part 2
def test_convert_many_words_to_numeric():
    ''' Given a string 4nineeightseven2
    When passed to the conversion function
    Then it returns 49872'''
    result = day_1.convert_words_to_numeric("4nineeightseven2")
    assert result == "49872"

def test_convert_2_words_to_numeric():
    ''' Given a string abcone2threexyz
    When passed to the conversion function
    Then it returns abc123xyz'''
    result = day_1.convert_words_to_numeric("abcone2threexyz")
    assert result == "abc123xyz"

def test_convert_1_word_to_numeric():
    ''' Given a string 7pqrstsixteen
    When passed to the conversion function
    Then it returns 7pqrst6teen'''
    result = day_1.convert_words_to_numeric("7pqrstsixteen")
    assert result == "7pqrst6teen"
