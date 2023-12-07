from aocd.models import Puzzle

RANKING = {"A": 14,
           "K": 13,
           "Q": 12,
           "J": 11,
           "T": 10,
           "9": 9,
           "8": 8,
           "7": 7,
           "6": 6,
           "5": 5,
           "4": 4,
           "3": 3,
           "2": 2}

def retrieve_puzzle_input():
    puzzle = Puzzle(year=2023, day=7)
    return puzzle.input_data

def parse_puzzle_input(puzzle_input):
    lines = puzzle_input.split("\n")
    bets_dict = {}
    for line in lines:
        halves = line.split(" ")
        bets_dict[halves[0]] = halves[1]
    return bets_dict

def quicksort(hands):
    if len(hands) <= 1:
        return hands
    else:
        pivot = len(hands) - 1
    greater = []
    lower = []
    for hand in hands[:pivot]:
        hand_1 = RANKING[hand[0]]
        hand_2 = RANKING[hand[1]]
        hand_3 = RANKING[hand[2]]
        hand_4 = RANKING[hand[3]]
        hand_5 = RANKING[hand[4]]
        pos_1 = RANKING[hands[pivot][0]]
        pos_2 = RANKING[hands[pivot][1]]
        pos_3 = RANKING[hands[pivot][2]]
        pos_4 = RANKING[hands[pivot][3]]
        pos_5 = RANKING[hands[pivot][4]]
        if hand_1 > pos_1:
            greater.append(hand)
        elif hand_1 == pos_1 and hand_2 > pos_2:
            greater.append(hand)
        elif hand[:2] == hands[pivot][:2] and hand_3 > pos_3:
            greater.append(hand)
        elif hand[:3] == hands[pivot][:3] and hand_4 > pos_4:
            greater.append(hand)
        elif hand[:4] == hands[pivot][:4] and hand_5 > pos_5:
            greater.append(hand)
        else:
            lower.append(hand)
    return quicksort(lower) + [hands[pivot]] + quicksort(greater)

def sort_hands(hands_list):
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []
    for hand in hands_list:
        hand_set = set(hand)
        set_check = len(hand_set)
        if set_check == 1: # all values the same, must be 5 of a kind
            five_of_a_kind.append(hand)
            continue
        if set_check == 2: # can be either 4 of a kind or full house
            counts = []
            for char in hand_set:
                counts.append(hand.count(char))
            if max(counts) == 4:
                four_of_a_kind.append(hand)
            else:
                full_house.append(hand)
        if set_check == 3: # can be either two pair or 3 of a kind
            counts = []
            for char in hand_set:
                counts.append(hand.count(char))
            if max(counts) == 3:
                three_of_a_kind.append(hand)
            else:
                two_pair.append(hand)
        if set_check == 4: # one duplicated value, must be one pair
            one_pair.append(hand)
            continue
        if set_check == 5: # no matches, must be high card
            high_card.append(hand)
            continue
    five_of_a_kind = quicksort(five_of_a_kind)
    four_of_a_kind = quicksort(four_of_a_kind)
    full_house = quicksort(full_house)
    three_of_a_kind = quicksort(three_of_a_kind)
    two_pair = quicksort(two_pair)
    one_pair = quicksort(one_pair)
    high_card = quicksort(high_card)
    return high_card + one_pair + two_pair + three_of_a_kind + full_house + four_of_a_kind + five_of_a_kind

def calculate_winnings(hand, bet, rank):
    return bet * rank

def total_winnings(sorted_hands,parsed_input):
    winnings = []
    for i,hand in enumerate(sorted_hands):
        rank = i+1
        bet = int(parsed_input[hand])
        winnings.append(calculate_winnings(hand,bet,rank))
    return sum(winnings)

def main():
    puzzle_input = retrieve_puzzle_input()
    bets_dict = parse_puzzle_input(puzzle_input)
    sorted_hands = sort_hands(bets_dict.keys())
    part1 = total_winnings(sorted_hands,bets_dict)
    return part1

if __name__ == "__main__":
    print(f"Answer to part 1: {main()}")
