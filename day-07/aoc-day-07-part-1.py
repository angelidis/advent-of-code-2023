# %% functions


def second_score(hand):
    # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
    # Numbers are less than letters so we are good to just return them
    letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}
    return [letter_map.get(char, char) for char in hand]


def score_type(hand):
    """
    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456
    """
    counts = [hand.count(card) for card in hand]

    # breakpoint()

    if len(hand) != 5:
        assert False, f"hand length is wrong ({hand}:{len(hand)})"

    if 5 in counts:
        return 10  # five of a kind
    if 4 in counts:
        return 9  # four of a kind
    if (3 in counts) and (2 in counts):
        return 8  # full house
    if (3 in counts) and (not 2 in counts):
        return 7  # three of a kind
    if (2 in counts) and (not 2 in counts):
        return 6  # three of a kind
    if counts.count(2) == 4:
        return 5  # two pair
    if 2 in counts:
        return 4  # one pair

    # for high card
    # counts will be [1, 1, 1, 1, 1]
    return 3


def score_hand(hand):
    return (score_type(hand), second_score(hand))


# %% main
file_path = "input.txt"
with open(file_path) as file:
    lines = [line.rstrip() for line in file]


plays = []
for line in lines:
    hand, bid = line.split()
    plays.append((hand, int(bid)))

plays.sort(key=lambda play: score_hand(play[0]))


total = 0

for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid


print(f"ans -> {total}")  # 247815719
