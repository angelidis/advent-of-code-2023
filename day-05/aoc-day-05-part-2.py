# %% functions


# %% main

file_path = "input.txt"
with open(file_path) as file:
    whole_file = file.read()

inpts, *blocks = whole_file.split("\n\n")

inpts = list(map(int, inpts.split(": ")[1].split()))

# lets create our seeds using [start, end) = [start, start+length) convention
seeds = []
for i in range(0, len(inpts), 2):
    seeds.append((inpts[i], inpts[i] + inpts[i + 1]))


print("initial seeds -> ", seeds)

for block in blocks:
    print(block)
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    print(ranges)

    new = []

    while len(seeds) > 0:
        strt, end = seeds.pop()  # order doesn't matter/pops off the LIFO

        # check for overlap in ranges
        for d, s, r in ranges:
            os = max(strt, s)  # overlap start
            oe = min(end, s + r)
            if os < oe:
                new.append((os + d - s, oe + d - s))
                if os > strt:
                    seeds.append((strt, os))
                if end > oe:
                    seeds.append((oe, end))
                break
        else:
            new.append((strt, end))

    print("old -> ", seeds)
    print("new -> ", new)
    seeds = new

# print(sorted(seeds))

ans = min(seeds)[0]
print(f"ans: {ans}")
