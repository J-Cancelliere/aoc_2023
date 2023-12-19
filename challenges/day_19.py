from aocd.models import Puzzle

def retrieve_puzzle_input():
    puzzle = Puzzle(year=2023, day=19)
    data = puzzle.input_data.split("\n\n")
    return data[0],data[1]

def parse_workflows(input_data):
    """Split the workflows into separate lines and parse each line into a
    key:value pair in a workflows dict. Each value will contain a list of
    tuples, and a single workflow key as the last element of the list"""
    workflow_dict= {}
    for line in input_data.split("\n"):
        # find key
        key_split = line.find("{")
        wf_key = line[:key_split]
        wf_values = line[key_split+1:-1].split(",")
        wf_tuples = []
        # parse tuple values
        for val in wf_values:
            # condition for last list item
            if len(val) < 4:
                wf_tuples.append((val,))
                continue
            source_key = val[0]
            comparison = val[1]
            number,destination = val[2:].split(":")
            wf_tuples.append((source_key,comparison,int(number),destination))
        workflow_dict[wf_key] = wf_tuples
    return workflow_dict

def parse_part_lists(input_data):
    """Split the part lists into separate lines and parse each line into a
    dict containing kay value pairs for each X-M-A-S part and its number.
    Returns a list of dicts"""
    part_list = []
    for line in input_data.split("\n"):
        xmas_list = line.strip("{").strip("}").split(",")
        xmas_dict = {}
        for part in xmas_list:
            key_val = part.split("=")
            xmas_dict[key_val[0]] = int(key_val[1])
        part_list.append(xmas_dict)
    return part_list

def accept_or_reject(workflows,part):
    """applies the workflows (starting with 'in') to one items dict.
    Returns boolean, True if accepted, False if rejected"""
    wf_key = "in"
    while True:
        for test in workflows[wf_key]:
            if len(test) == 1:
                if test[0] == "A":
                    return True
                elif test[0] == "R":
                    return False
                else:
                    wf_key = test[0]
                    break
            part_key = test[0]
            if test[1] == ">":
                if part[part_key] > test[2]:
                    if test[-1] == "A":
                        return True
                    elif test[-1] == "R":
                        return False
                    else:
                        wf_key = test[-1]
                        break
            if test[1] == "<":
                if part[part_key] < test[2]:
                    if test[-1] == "A":
                        return True
                    elif test[-1] == "R":
                        return False
                    else:
                        wf_key = test[-1]
                        break

def find_permutations(workflows):
    start_values = {"x":4000,"m":4000,"a":4000,"s":4000}
    A = {"x":0,"m":0,"a":0,"s":0}
    R = {"x":0,"m":0,"a":0,"s":0}
    wf_key = "in"
    pass

def p1_final_sum(accepted_list):
    total = 0
    for part in accepted_list:
        total += sum(part.values())
    return total

def main():
    raw_workflows, raw_parts = retrieve_puzzle_input()
    workflow_list = parse_workflows(raw_workflows)
    part_list = parse_part_lists(raw_parts)
    accepted_parts = []
    for part in part_list:
        if accept_or_reject(workflow_list,part):
            accepted_parts.append(part)
    p1_answer = p1_final_sum(accepted_parts)
    return f"Answer to part 1: {p1_answer}"

if __name__ == "__main__":
    print(main())
