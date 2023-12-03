# %% functions


# %% main

# cs: coordinate set
# ns: number set

file_path = "input0.txt"
with open(file_path) as file:
    grid = [line.rstrip() for line in file]


cs = set()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        # scanning for symbols
        if ch.isdigit() or ch == ".":
            continue

        # you have a symbol, scan the area around it
        for cr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                # if you are out of bounds or it's not a digit skip it!
                if (
                    cr < 0
                    or cr >= len(grid)
                    or cc < 0
                    or cc >= len(grid[cr])
                    or not grid[cr][cc].isdigit()
                ):
                    continue

                # scan to the beginning of the number
                while cc > 0 and grid[cr][cc - 1].isdigit():
                    cc -= 1
                cs.add((cr, cc))

print(cs)

# convert coordinate set into the actual numbers
ns = []
for r, c in cs:
    s = ""
    # scan to the right
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    ns.append(int(s))


ans = sum(ns)
print(f"{ans}")
