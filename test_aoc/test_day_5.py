from challenges import day_5

test_input='''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

# part 1 tests: almanac progression
# Seed 79,          Seed 14             Seed 55             Seed 13
#   soil 81             soil 14            soil 57             soil 13
#   fertilizer 81       fertilizer 53      fertilizer 57       fertilizer 52
#   water 81            water 49           water 53            water 41
#   light 74            light 42           light 46            light 34
#   temperature 78      temperature 42     temperature 82      temperature 34
#   humidity 78         humidity 43        humidity 82         humidity 35
#   location 82.        location 43.       location 86.        location 35.

test_seeds, test_input_parsed = day_5.parse_puzzle_input(test_input)

# Not making this function - real input data is too big
# mappings = day_5.make_mappings(test_input_parsed)

def test_below_start_mapping():
    # given source number 14 and mapping (18, 25, 70)
    # when converting the soure number
    # return destination 14
    result = day_5.convert_number(14,(18, 25, 70))
    assert result == 14



def test_above_range_mapping():
    # given source number 81 and mapping (0, 11, 42)
    # when converting the soure number
    # return destination 81
    result = day_5.convert_number(81,(0, 11, 42))
    assert result == 81

def test_within_range_mapping():
    # given source number 81 and mapping (18, 25, 70)
    # when converting the soure number
    # return destination 74
    result = day_5.convert_number(81,(18, 25, 70))
    assert result == 74

def test_lowest_loc():
    # given the test input above
    # when searching the lowest location number
    # return 35
    seed_catalogue = day_5.catalogue_seed_data(test_seeds,test_input_parsed)
    result = day_5.get_lowest_loc(seed_catalogue)
    assert result == 35
