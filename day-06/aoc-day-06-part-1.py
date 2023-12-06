# %% functions


# %% main

file_path = "input.txt"
with open(file_path) as file:
    lines = [line.rstrip() for line in file]

times, distances = [list(map(int, line.split(":")[1].strip().split())) for line in lines]

ans = 1  # product of how many we can win the race

# hold_speed = hold x ms --> x mm/ms
# distance traveled = rem_time * hold_speed

for time, distance in zip(times, distances):
    margin = 0
    for hold in range(time):
        if hold * (time - hold) > distance:
            margin += 1

    ans *= margin
    print(margin)


print(f"ans -> {ans}")
