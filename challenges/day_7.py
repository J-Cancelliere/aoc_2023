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

RANKING2 = {"A": 14,
           "K": 13,
           "Q": 12,
           "T": 10,
           "9": 9,
           "8": 8,
           "7": 7,
           "6": 6,
           "5": 5,
           "4": 4,
           "3": 3,
           "2": 2,
           "J": 1}

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

def quicksort(hands, rank):
    if len(hands) <= 1:
        return hands
    else:
        pivot = len(hands) - 1
    greater = []
    lower = []
    for hand in hands[:pivot]:
        hand_1 = rank[hand[0]]
        hand_2 = rank[hand[1]]
        hand_3 = rank[hand[2]]
        hand_4 = rank[hand[3]]
        hand_5 = rank[hand[4]]
        pos_1 = rank[hands[pivot][0]]
        pos_2 = rank[hands[pivot][1]]
        pos_3 = rank[hands[pivot][2]]
        pos_4 = rank[hands[pivot][3]]
        pos_5 = rank[hands[pivot][4]]
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
    return quicksort(lower, rank) + [hands[pivot]] + quicksort(greater, rank)

def sort_hands(hands_list):
    five = []
    four = []
    full = []
    three = []
    pair2 = []
    pair1 = []
    high = []
    for hand in hands_list:
        hand_set = set(hand)
        set_check = len(hand_set)
        if set_check == 1: # all values the same, must be 5 of a kind
            five.append(hand)
            continue
        if set_check == 2: # can be either 4 of a kind or full house
            counts = []
            for char in hand_set:
                counts.append(hand.count(char))
            if max(counts) == 4:
                four.append(hand)
            else:
                full.append(hand)
        if set_check == 3: # can be either two pair or 3 of a kind
            counts = []
            for char in hand_set:
                counts.append(hand.count(char))
            if max(counts) == 3:
                three.append(hand)
            else:
                pair2.append(hand)
        if set_check == 4: # one duplicated value, must be one pair
            pair1.append(hand)
            continue
        if set_check == 5: # no matches, must be high card
            high.append(hand)
            continue
    five = quicksort(five, RANKING)
    four = quicksort(four, RANKING)
    full = quicksort(full, RANKING)
    three = quicksort(three, RANKING)
    pair2 = quicksort(pair2, RANKING)
    pair1 = quicksort(pair1, RANKING)
    high = quicksort(high, RANKING)
    keys = ["high", "pair1", "pair2", "three", "full", "four", "five"]
    result = [high, pair1, pair2, three, full, four, five]
    return dict(zip(keys,result))

def find_all_jokers(type_dict):
    joker_list = []
    new_dict = {}
    for key in type_dict.keys():
        for i,hand in enumerate(type_dict[key]):
            if hand.find("J") != -1:
                joker_list.append(hand)
            else:
                if new_dict.get(key):
                    new_dict[key].append(hand)
                else:
                    new_dict[key] = [hand]
    new_dict["jokers"] = joker_list
    return new_dict

def sort_jokers(joker_dict):
    for joker in joker_dict["jokers"]:
        j_set = set(joker)
        counts = {}
        for char in j_set:
            counts[char] = joker.count(char)
        if len(counts) == 5:
            joker_dict["pair1"].append(joker)
            continue
        if len(counts) == 4:
            joker_dict["three"].append(joker)
            continue
        if len(counts) == 3:
            if counts["J"] == 3:
                joker_dict["four"].append(joker)
                continue
            if counts["J"] == 2:
                joker_dict["four"].append(joker)
                continue
            if counts["J"] == 1:
                if 3 in counts.values():
                    joker_dict["four"].append(joker)
                else:
                    joker_dict["full"].append(joker)
                continue
        if len(counts) == 2:
            if not joker_dict.get("five"):
                joker_dict["five"] = [joker]
            else:
                joker_dict["five"].append(joker)
            continue
        if len(counts) == 1:
            if not joker_dict.get("five"):
                joker_dict["five"] = [joker]
            else:
                joker_dict["five"].append(joker)
            continue
    sorted_hands = []
    for key in joker_dict.keys():
        if key == "jokers":
            continue
        sorted_hands.extend(quicksort(joker_dict[key],RANKING2))
    return sorted_hands

def calculate_winnings(hand, bet, rank):
    return bet * rank

def total_winnings(hand_list,parsed_input):
    winnings = []
    for i,hand in enumerate(hand_list):
        # print(hand)
        rank = i+1
        bet = int(parsed_input[hand])
        winnings.append(calculate_winnings(hand,bet,rank))
    return sum(winnings)

def main():
    puzzle_input = retrieve_puzzle_input()
    bets_dict = parse_puzzle_input(puzzle_input)
    sorted_hands = sort_hands(bets_dict.keys())
    # part1 = total_winnings(sorted_hands.values(),bets_dict)
    jokers = find_all_jokers(sorted_hands)
    sorted_jokers = sort_jokers(jokers)
    part2 = total_winnings(sorted_jokers,bets_dict)
    # return part1
    return part2

if __name__ == "__main__":
    print(f"Answers: {main()}")
