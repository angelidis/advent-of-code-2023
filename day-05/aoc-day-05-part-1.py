# %% functions


# %% main

file_path = "input.txt"
with open(file_path) as file:
    whole_file = file.read()

seeds, *blocks = whole_file.split("\n\n")

seeds = list(map(int, seeds.split(": ")[1].split()))

print("initial seeds -> ", seeds)

for block in blocks:
    print(block)
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    print(ranges)

    new = []
    for x in seeds:
        for d, s, r in ranges:
            # equiv to x in range(s, s+r)
            if s <= x < s + r:
                new.append(d + x - s)
                break
        else:
            new.append(x)

    print("old -> ", seeds)
    print("new -> ", new)
    seeds = new


ans = min(seeds)
print(f"ans: {ans}")