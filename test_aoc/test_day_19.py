from challenges import day_19

test_input1 = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}"""

test_input2 = """{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

# part 1 tests

def test_workflow_parser():
    # given test_input1
    # when parsing the data
    # return a dict with workflows as keys, and workflows as a list of tuples.
    result = day_19.parse_workflows(test_input1)
    assert list(result.keys())[0] == "px"
    assert result["px"][0][0] == "a"
    assert result["px"][0][1] == "<"
    assert result["px"][0][2] == 2006
    assert result["px"][0][3] == "qkq"
    assert result["px"][-1] == ("rfg",)

def test_parts_parser():
    # given test_input1
    # when parsing the data
    # return a list of dicts with part letter as key, number as value
    result = day_19.parse_part_lists(test_input2)
    assert result[0].get("x") == 787
    assert result[2].get("a") == 79
    assert result[-1].get("s") == 1013
    assert len(result[0]) == 4

def test_accept():
    # given the first part dict test_data2 and workflows
    # when running through workflows
    # return True
    part = {"x":787,"m":2655,"a":1222,"s":2876}
    workflows = day_19.parse_workflows(test_input1)
    result = day_19.accept_or_reject(workflows,part)
    assert result == True

def test_reject():
    # given the second part dict test_data2 and workflows
    # when running through workflows
    # return False
    part = {"x":1679,"m":44,"a":2067,"s":496}
    workflows = day_19.parse_workflows(test_input1)
    result = day_19.accept_or_reject(workflows,part)
    assert result == False

def test_final_sum():
    # given a list of accepted parts
    # when caluclating the total sum of their values
    # return 19114
    part_list = [
        {"x":787,"m":2655,"a":1222,"s":2876},
        {"x":2036,"m":264,"a":79,"s":2244},
        {"x":2127,"m":1623,"a":2188,"s":1013}
    ]
    result = day_19.p1_final_sum(part_list)
    assert result == 19114

# part 2 tests

def test_find_permutations():
    # given the test_data1
    # When calcualting the total possible accepted,
    # return 167409079868000
    workflows = day_19.parse_workflows(test_input1)
    result = day_19.find_permutations(workflows)
    assert result == 167409079868000
