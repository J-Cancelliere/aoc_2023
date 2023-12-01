from aocd.models import Puzzle

# Mapping of written words to numemric values
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
    '''Retrieve the input data
    Parameters: none
    Output: Returns the input as a list of strings'''
    data = Puzzle(year=2023, day=1)
    return data.input_data.split("\n")

def convert_words_to_numeric(line):
    '''Add in the numeric value of any numbers included as full words
    Parameters:
    - line: a string containing both letters and numbers (numeric and words)
    Output: Returns the string with any spelled out numbers added as digits'''
    for word in WORDS.keys():
        # Allows for multiple str.find() functions until all instances are found
        still_searching = True
        while still_searching == True:
            word_loc = line.find(word)
            if word_loc == -1:
                still_searching = False
                continue
            line = line[:word_loc+1] + WORDS[word] + line[word_loc+1:]
    return line

def extract_calibration_values(line):
    '''Find the first and last occurring numbers in a string
    Parameters:
    - line: a string containing both numbers and letters
    Output: Returns the first and last digits from the string as a single int'''
    line_len = len(line)
    calibration = {}
    # searching forwards and backwards simultaneously
    for i in range(line_len):
        front = i
        back = (i * -1) - 1 if i > 0 else -1 # because 0 * -1 = 0
        if line[front].isnumeric() and not calibration.get("front"):
            calibration["front"] = line[front]
        if line[back].isnumeric() and not calibration.get("back"):
            calibration["back"] = line[back]
    return int(calibration["front"] + calibration["back"])

def collect_all_values(data, words=False):
    '''Collate the calibration values from every line in the input data
    Parameters:
    - data: a list of input strings. Each list element is a single string.
    - words: boolean. When set to True, the function calls
    convert_words_to_numeric function before collating the final integer list
    Output: Returns a list of integers'''
    if words == True:
        converted_values = [convert_words_to_numeric(datum) for datum in data]
        return [extract_calibration_values(value) for value in converted_values]
    return [extract_calibration_values(datum) for datum in data]

def sum_calibration_values(calibration_list):
    '''Generate the total value of all the integers in the list
    Parameters: Accepts a list of integers
    Output: Returns the sum of the input list as a single int'''
    return sum(calibration_list)

def main():
    data = retrieve_challenge_input()
    calibration_list = collect_all_values(data, words= True)
    return sum_calibration_values(calibration_list)

if __name__ == "__main__":
    print(main())
