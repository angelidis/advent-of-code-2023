def proc_lines(line):
    res = list(filter(str.isdigit, line))  # the digits are repr as strings
    if len(res) > 1:
        resn = int(f"{res[0]}{res[-1]}")
    else:
        resn = int(res[0] * 2)

    return resn


file_path = "input.txt"
with open(file_path) as file:
    lines = [line.rstrip() for line in file]

numbs = []
for line in lines:
    resn = proc_lines(line)
    numbs.append(resn)

answer = sum(numbs)
print(answer)
