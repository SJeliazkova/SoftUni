wagons = int(input())

train = [0 for el in range(wagons)]

command = input()

while command != "End":
    data = command.split()

    if data[0] == "add":
        train[-1] += int(data[1])
    elif data[0] == "insert":
        index = int(data[1])
        num_of_people = int(data[2])
        train[index] += num_of_people
    elif data[0] == "leave":
        index = int(data[1])
        num_of_people = int(data[2])
        train[index] -= num_of_people

    command = input()

print(train)