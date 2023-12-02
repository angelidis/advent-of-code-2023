# %% functions


def multiply_list(mylist):
    result = 1
    for x in mylist:
        result *= x
    return result


# %% main

import string

file_path = "input.txt"
with open(file_path) as file:
    lines = [line.rstrip() for line in file]

ans = 0
winnable_games = 0

power_sum = 0

for line in lines:
    # breakpoint()
    min_balls_for_game = {"red": 0, "green": 0, "blue": 0}

    game, line = line.split(":")
    id_ = int(game.strip(string.ascii_letters))

    for event in line.split(";"):
        for balls in event.strip().split(","):
            n, color = balls.strip().split(" ")

            if int(n) > min_balls_for_game.get(color, 0):
                min_balls_for_game[color] = int(n)

    power_game_i = multiply_list(min_balls_for_game.values())

    print(f"{game}: {power_game_i}")

    power_sum += power_game_i

print(f"sum: {power_sum}")
