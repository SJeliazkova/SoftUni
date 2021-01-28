neighborhood = list(map(int, input().split("@")))

command = input()
last_position = 0

while command != "Love!":
    jump, step = command.split()
    step = int(step)

    current_index = last_position + step
    if current_index >= len(neighborhood):
        current_index = 0

    if neighborhood[current_index] > 0:
        neighborhood[current_index] -= 2

        if neighborhood[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")
    else:
        print(f"Place {current_index} already had Valentine's day.")

    last_position = current_index

    command = input()

print(f"Cupid's last position was {last_position}.")

if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    no_valentine_day = len(neighborhood) - neighborhood.count(0)
    print(f"Cupid has failed {no_valentine_day} places.")