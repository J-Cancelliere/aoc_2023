from challenges import day_7

test_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# tests for part 1

def test_order_of_cards():
    # given a list of cards: 32T3K, T55J5, KK677, KTJJT, QQQJA
    # when ordering the ranks
    # return 32T3K, KTJJT, KK677, T55J5, QQQJA
    result = day_7.sort_hands(["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"])
    assert result == ["32T3K", "KTJJT", "KK677", "T55J5", "QQQJA"]

def test_value_of_one_hand():
    # given a hand of cards QQQJA with bet 483 and rank 5
    # when calculating winnings
    # return 2415
    result = day_7.calculate_winnings("QQQJA", 483, 5)
    assert result == 2415

def test_sum_all_products():
    # given the above test data
    # when compiling the total winnings
    # return 6440
    sorted_hands = day_7.sort_hands(["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"])
    test_parsed = day_7.parse_puzzle_input(test_data)
    result = day_7.total_winnings(sorted_hands,test_parsed)
    assert result == 6440

# tests for part 2

def test_new_categorizer():
    # given a list of cards: 32T3K, T55J5, KK677, KTJJT, QQQJA
    # when ordering the ranks
    # return 32T3K, KTJJT, KK677, T55J5, QQQJA
    result = day_7.sort_hands(["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"])
    assert result == ["32T3K", "KK677", "T55J5", "QQQJA", "KTJJT"]
