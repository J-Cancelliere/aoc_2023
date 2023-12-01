from aocd.models import Puzzle

def retrieve_challenge_input():
    data = Puzzle(year=2023, day=1)
    return data.input_data.split("\n")

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

def collect_all_values(data):
    return [extract_calibration_values(datum) for datum in data]

def sum_calibration_values(calibration_list):
    return sum(calibration_list)

def main():
    data = retrieve_challenge_input()
    calibration_list = collect_all_values(data)
    return sum_calibration_values(calibration_list)

if __name__ == "__main__":
    print(main())
