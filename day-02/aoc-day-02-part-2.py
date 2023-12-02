# %% functions


# %% main
from collections import defaultdict

import string

file_path = "input.txt"
with open(file_path) as file:
    lines = [line.rstrip() for line in file]


power_sum = 0

for line in lines:
    min_balls_for_game = defaultdict(int)

    game, line = line.split(":")
    id_ = int(game.strip(string.ascii_letters))

    for event in line.split(";"):
        for balls in event.strip().split(","):
            n, color = balls.strip().split(" ")
            min_balls_for_game[color] = max(min_balls_for_game[color], int(n))

    power_game_i = 1
    for val in min_balls_for_game.values():
        power_game_i *= val

    print(f"{game}: {power_game_i}")

    power_sum += power_game_i

print(f"sum: {power_sum}")
