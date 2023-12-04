# %% functions


# %% main
from collections import defaultdict

file_path = "input.txt"
with open(file_path) as file:
    cards = [line.rstrip() for line in file]

total_cards = defaultdict(int)

score = 0

for c, card in enumerate(cards):
    total_cards[c + 1] += 1
    print(f"Running for card #{c+1}")

    tit, lists = card.split(": ")
    wl, ml = [list(map(int, ll.split())) for ll in lists.split(" | ")]

    matches = 0

    for n, wnum in enumerate(wl):
        for i, mnum in enumerate(ml):
            if wnum == mnum:
                matches += 1

    # print("before: ", total_cards)
    # print(f"#{c+1} has {matches} matches")

    for i in range(c + 1 + 1, c + 1 + 1 + matches):
        total_cards[i] += 1 * total_cards[c + 1]

    # print("after:", total_cards)
    # print("\n\n")

score = sum(total_cards.values())

print(f"{score}")
