# %% functions


# %% main
import string

file_path = "input.txt"
with open(file_path) as file:
    lines = [line.rstrip() for line in file]

# only 12 red cubes, 13 green cubes, and 14 blue cubes

ans = 0
winnable_games = 0

for line in lines:
    ok = True

    game, line = line.split(":")
    id_ = int(game.strip(string.ascii_letters))

    # print(game)

    for event in line.split(";"):
        for balls in event.strip().split(","):
            n, color = balls.strip().split(" ")

            if int(n) > {"red": 12, "green": 13, "blue": 14}.get(color, 0):
                ok = False

    if ok:
        winnable_games += 1
        ans += id_

    # print("=" * 80)


print(f"possible games: {winnable_games}")
print(f"correct answer: {ans}")
