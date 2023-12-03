from challenges import day_3

test_input = '''467..114..
                ...*......
                ..35..633.
                ......#...
                617*......
                .....+.58.
                ..592.....
                ......755.
                ...$.*....
                .664.598..'''

test_list = test_input.split("\n")

test_dict = {k:test_list[k].strip() for k in range(0,10)}

def test_search_lines():
    '''When searching the test_dict
    Then the function returns 4361'''
    result = day_3.search_lines(test_dict)
    assert result == 4361
