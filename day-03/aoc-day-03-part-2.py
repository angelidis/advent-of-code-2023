# %% functions


# %% main

# cs: coordinate set
# ns: number set

file_path = "input.txt"
with open(file_path) as file:
    grid = [line.rstrip() for line in file]

total = 0

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch != "*":
            continue

        cs = set()

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

        if len(cs) != 2:
            continue

        ns = []
        for cr, cc in cs:
            s = ""
            # scan to the right
            while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                s += grid[cr][cc]
                cc += 1
            ns.append(int(s))

        total += ns[0] * ns[1]

print(f"{total}")
