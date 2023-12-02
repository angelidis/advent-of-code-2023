# %% functions


def score_line(line):
    score = 0
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)

        for d, val in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        ):
            if line[i:].startswith(val):
                digits.append(str(d + 1))

    score = int(digits[0] + digits[-1])

    return score


# %% main

file_path = "input_part2.txt"
with open(file_path) as file:
    lines = [line.rstrip() for line in file]

answer = 0
numbs3 = []
for line in lines:
    score = score_line(line)

    numbs3.append(score)

answer = sum(numbs3)
print(answer)  # 54100 is the right


# %% test me
res = {
    "two1nine": 29,
    "eightwothree": 83,
    "abcone2threexyz": 13,
    "xtwone3four": 24,
    "4nineeightseven2": 42,
    "zoneight234": 14,
    "7pqrstsixteen": 76,
    "fivezg8jmf6hrxnhgxxttwoneg": 51,
    "fivegdsfnfour64sixtqfour": 54,
}
for k, v in res.items():
    test_res = proc_lines(fix_line(k)) - v
    print(f"{v} {test_res}")
