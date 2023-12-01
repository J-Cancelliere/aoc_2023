from aocd.models import Puzzle

WORDS = {"one": "1",
         "two": "2",
         "three": "3",
         "four": "4",
         "five": "5",
         "six": "6",
         "seven": "7",
         "eight": "8",
         "nine": "9"}

def retrieve_challenge_input():
    data = Puzzle(year=2023, day=1)
    return data.input_data.split("\n")

def convert_words_to_numeric(line):
    for word in WORDS.keys():
        still_searching = True
        while still_searching == True:
            word_loc = line.find(word)
            if word_loc == -1:
                still_searching = False
                continue
            line = line[:word_loc+1] + WORDS[word] + line[word_loc+1:]
    return line

def extract_calibration_values(line):
    line_len = len(line)
    calibration = {}
    for i in range(line_len):
        front = i
        back = (i * -1) - 1 if i > 0 else -1
        if line[front].isnumeric() and not calibration.get("front"):
            calibration["front"] = line[front]
        if line[back].isnumeric() and not calibration.get("back"):
            calibration["back"] = line[back]
    return int(calibration["front"] + calibration["back"])

def collect_all_values(data, words=False):
    if words == True:
        converted_values = [convert_words_to_numeric(datum) for datum in data]
        return [extract_calibration_values(value) for value in converted_values]
    return [extract_calibration_values(datum) for datum in data]

def sum_calibration_values(calibration_list):
    return sum(calibration_list)

def main():
    data = retrieve_challenge_input()
    calibration_list = collect_all_values(data, words= True)
    return sum_calibration_values(calibration_list)

if __name__ == "__main__":
    print(main())
