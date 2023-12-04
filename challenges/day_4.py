from aocd.models import Puzzle

def retrieve_puzzle_input():
    puzzle = Puzzle(year=2023, day=4)
    return puzzle.input_data

def process_input(data):
    ''' Split each line fron puzzle input into a dictionary:
    The game number is the dict key, and ever value is a tuple
    Tuples are a triple value containing a list of winning numbers, numbers,
    and the assumed point value of the card (always starts at 0)'''
    lines = data.split("\n")
    card_dict = {}
    for line in lines:
        divide = line.split(":")
        key = divide[0]
        numbers = divide[1].split("|")
        winners = numbers[0].split(" ")
        scratches = numbers[1].split(" ")
        winners = [int(w) for w in winners if w.isnumeric()]
        scratches = [int(s) for s in scratches if s.isnumeric()]
        card_dict[key] = (winners,scratches,0)
    return card_dict

def get_point_value(card):
    '''Takes one card (3-tuple) and determines the point value of the card.
    Returns the same tuple with the known point value'''
    winners = card[0]
    scratches = card[1]
    value = card[2]
    for s in scratches:
        for w in winners:
            if s - w == 0:
                if value == 0:
                    value += 1
                    break
                value *= 2
                break
    return (winners,scratches,value)

def main():
    data = retrieve_puzzle_input()
    cards_dict = process_input(data)
    total_points = 0
    for card in cards_dict.values():
        value = get_point_value(card)
        total_points += value[2]
    return total_points

if __name__ == "__main__":
    print(main())
