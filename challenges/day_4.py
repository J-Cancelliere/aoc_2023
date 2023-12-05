from aocd.models import Puzzle

def retrieve_puzzle_input():
    puzzle = Puzzle(year=2023, day=4)
    return puzzle.input_data

def process_input(data):
    ''' Split each line fron puzzle input into a dictionary:
    The game number is the dict key, and ever value is a tuple
    Tuples contains 5 values:
    - a list of winning numbers
    - the scratched numbers
    - the assumed point value of the card (always starts at 0)
    - the number of matches (always starts at 0)
    - the number of copies (always starts at 1)'''
    lines = data.split("\n")
    card_dict = {}
    for line in lines:
        divide = line.split(":")
        key = int(divide[0].strip("Card "))
        numbers = divide[1].split("|")
        winners = numbers[0].split(" ")
        scratches = numbers[1].split(" ")
        winners = [int(w) for w in winners if w.isnumeric()]
        scratches = [int(s) for s in scratches if s.isnumeric()]
        card_dict[key] = (winners,scratches,0,0,1)
    return card_dict

def get_point_value(card):
    '''Takes one card (4-tuple) and determines the point value of the card.
    Returns the same tuple with the known point value'''
    winners, scratches, value, matches, copies = card
    for s in scratches:
        for w in winners:
            if s - w == 0:
                if value == 0:
                    value += 1
                    break
                value *= 2
                break
    return (winners, scratches, value, matches, copies)

def get_copy_counts(card_dict):
    '''TODO: The while loop in the second half of this function is very
    comutationally expensive (~15 seconds). Consider reconfiguirng to run
    faster.
    Iterates over the dictionary once to count the number of matches
    Iterates over the dictionary a second time to update the number of copies
    for each card.
    Returns a single int, the total number of copies in the dict'''
    upper_limit = len(card_dict)
    card_dict_updated = {}
    # Update card_dict to contain correc number of matches
    for i in range(1,upper_limit+1):
        line = get_point_value(card_dict[i])
        winners, scratches, value, matches, copies = line
        loop_value = value
        while loop_value > 0:
            if loop_value == 1:
                loop_value -= 1
            loop_value /= 2
            matches += 1
        card_dict_updated[i] = (winners, scratches, value, matches, copies)
    total_scratchcards = 0
    for i in range(1,upper_limit+1):
        line = card_dict_updated[i]
        winners, scratches, value, matches, copies = line
        copy_looper = copies
        print(f"Updating card number {i}")
        while copy_looper > 0:
            for j in range(1,matches+1):
                # convert tuple to list for reassignment
                card_update = list(card_dict_updated[i+j])
                card_update[4] += 1
                card_dict_updated[i+j] = tuple(card_update)
            copy_looper -= 1
        total_scratchcards += copies
    return total_scratchcards

def main():
    data = retrieve_puzzle_input()
    cards_dict = process_input(data)
    part1_answer = 0
    for card in cards_dict.values():
        value = get_point_value(card)
        part1_answer += value[2]
    part2_answer = get_copy_counts(cards_dict)
    return (part1_answer,part2_answer)

if __name__ == "__main__":
    part1, part2 = main()
    print(f"Answer to part 1: {part1}")
    print(f"Answer to part 2: {part2}")
