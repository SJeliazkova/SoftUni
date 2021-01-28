targets = list(map(int, input().split("|")))

data = input()
points = 0

while not data == "Game over":

    if data == "Reverse":
        targets = targets[::-1]
    else:
        command = data.split("@")[0]
        start_index = int(data.split("@")[1])
        length = int(data.split("@")[2])

        if start_index in range(len(targets)):

            if command == "Shoot Left":
                shoot_index = (start_index - length) % len(targets)

            elif command == "Shoot Right":
                shoot_index = (start_index + length) % len(targets)

            if targets[shoot_index] < 5:
                points += targets[shoot_index]
                targets[shoot_index] = 0
            else:
                points += 5
                targets[shoot_index] -= 5

    data = input()

print(' - '.join(map(str, targets)))
print(f"Iskren finished the archery tournament with {points} points!")



