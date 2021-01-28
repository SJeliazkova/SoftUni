sugar_cubes = list(map(int, input().split()))

command = input()

while not command == "Mort":
    type_command = command.split()[0]
    value = int(command.split()[1])

    if type_command == "Add":
        sugar_cubes.append(value)

    elif type_command == "Remove":
        sugar_cubes.remove(value)

    elif type_command == "Replace":
        replacement = int(command.split()[2])
        index_replace = sugar_cubes.index(value)
        sugar_cubes[index_replace] = replacement

    elif type_command == "Collapse":
        sugar_cubes = [cube for cube in sugar_cubes if cube >= value]

    command = input()

print(' '.join([str(el) for el in sugar_cubes]))

