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
