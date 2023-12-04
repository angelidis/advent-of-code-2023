# %% functions


# %% main

file_path = "input.txt"
with open(file_path) as file:
    cards = [line.rstrip() for line in file]


stack_val = 0  # stack of cards

for c, card in enumerate(cards):
    tit, lists = card.split(": ")
    wl, ml = [list(map(int, ll.split())) for ll in lists.split(" | ")]

    matched = 0
    card_val = 0

    for n, wnum in enumerate(wl):
        for i, mnum in enumerate(ml):
            if wnum == mnum:
                matched += 1

    if matched:
        card_val = 2 ** (matched - 1)

    stack_val += card_val
    # print(f"{tit} - {card_val}\n")

print(f"{stack_val}")
