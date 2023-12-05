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

test_seeds, test_input_parsed = day_5.parse_puzzle_input()

mappings = day_5.make_mappings()

def test_convert_seed_soil():
    # for seeds 79, 14, 55, 13
    # when converting to soil
    # then return 81, 14, 57, 13
    result1 = day_5.convert_number(79,mappings["soil"])
    assert result1 == 81
    result2 = day_5.convert_number(14,mappings["soil"])
    assert result2 == 14
    result2 = day_5.convert_number(55,mappings["soil"])
    assert result2 == 57
    result4 = day_5.convert_number(13,mappings["soil"])
    assert result4 == 13

def test_convert_soil_fert():
    # for soils 81, 14, 57, 13
    # when converting to fertilizer
    # then return 81, 53, 57, 52
    result1 = day_5.convert_number(81,mappings["fertilizer"])
    assert result1 == 81
    result2 = day_5.convert_number(14,mappings["fertilizer"])
    assert result2 == 53
    result2 = day_5.convert_number(57,mappings["fertilizer"])
    assert result2 == 57
    result4 = day_5.convert_number(13,mappings["fertilizer"])
    assert result4 == 52

def test_convert_fert_water():
    # for fertilizers 81, 53, 57, 52
    # when converting to water
    # then return 81, 49, 53, 41
    result1 = day_5.convert_number(81,mappings["water"])
    assert result1 == 81
    result2 = day_5.convert_number(53,mappings["water"])
    assert result2 == 49
    result2 = day_5.convert_number(57,mappings["water"])
    assert result2 == 53
    result4 = day_5.convert_number(52,mappings["water"])
    assert result4 == 41

def test_convert_water_light():
    # for waters 81, 49, 53, 41
    # when converting to light
    # then return 74, 42, 46, 34
    result1 = day_5.convert_number(81,mappings["light"])
    assert result1 == 74
    result2 = day_5.convert_number(49,mappings["light"])
    assert result2 == 42
    result2 = day_5.convert_number(46,mappings["light"])
    assert result2 == 46
    result4 = day_5.convert_number(34,mappings["light"])
    assert result4 == 34

def test_convert_light_temp():
    # for lights 74, 42, 46, 34
    # when converting to temp
    # then return 78, 42, 82, 34
    result1 = day_5.convert_number(74,mappings["temp"])
    assert result1 == 78
    result2 = day_5.convert_number(42,mappings["temp"])
    assert result2 == 42
    result2 = day_5.convert_number(46,mappings["temp"])
    assert result2 == 82
    result4 = day_5.convert_number(34,mappings["temp"])
    assert result4 == 34

def test_convert_temp_humid():
    # for temps 78, 42, 82, 34
    # when converting to humidity
    # then return 78, 43, 82, 35
    result1 = day_5.convert_number(78,mappings["temp"])
    assert result1 == 78
    result2 = day_5.convert_number(42,mappings["temp"])
    assert result2 == 43
    result2 = day_5.convert_number(82,mappings["temp"])
    assert result2 == 82
    result4 = day_5.convert_number(34,mappings["temp"])
    assert result4 == 35

def test_convert_humid_loc():
    # for temps 78, 43, 82, 35
    # when converting to humidity
    # then return 82, 43, 86, 35
    result1 = day_5.convert_number(78,mappings["temp"])
    assert result1 == 82
    result2 = day_5.convert_number(43,mappings["temp"])
    assert result2 == 43
    result2 = day_5.convert_number(82,mappings["temp"])
    assert result2 == 86
    result4 = day_5.convert_number(35,mappings["temp"])
    assert result4 == 35

seed_catalogue = day_5.catalogue_seed_data(test_seeds)

def test_lowest_loc():
    # given the test input above
    # when searching the lowest location number
    # return 35
    result = day_5.get_lowest_loc(seed_catalogue)
