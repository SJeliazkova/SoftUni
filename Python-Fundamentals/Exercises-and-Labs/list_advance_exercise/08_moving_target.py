targets = list(map(int, input().split()))

data = input()

while data != "End":
    command, index, value = data.split()
    index = int(index)
    value = int(value)

    if command == "Shoot":
        if index in range(len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif command == "Add":
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        left_index = index - value
        right_index = index + value
        if left_index >= 0 and right_index < len(targets):
            left_part = targets[:left_index]
            right_part = targets[right_index + 1:]
            targets = left_part + right_part
        else:
            print("Strike missed!")

    data = input()

print("|".join([str(el) for el in targets]))