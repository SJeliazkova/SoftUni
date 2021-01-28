targets = input().split()
targets = list(map(int, targets))

command = input()
counter = 0

while not command == "End":
    current_index = int(command)

    if current_index in range(len(targets)):
        shoot_target = targets[current_index]

        for index in range(len(targets)):
            if targets[index] > shoot_target and targets[index] != -1:
                targets[index] -= shoot_target
            elif targets[index] <= shoot_target and targets[index] != -1:
                targets[index] += shoot_target

        targets[current_index] = -1
        counter += 1

    command = input()

print(f"Shot targets: {counter} -> {' '.join([str(el) for el in targets])}")





