array = list(map(int, input().split()))

data = input()

while not data == "end":
    if data == "decrease":
        for i in range(len(array)):
            array[i] -= 1

    else:
        command = data.split()[0]
        index_1 = int(data.split()[1])
        index_2 = int(data.split()[2])

        if command == "swap":
            array[index_1], array[index_2] = array[index_2], array[index_1]

        elif command == "multiply":
            new_item = array[index_1] * array[index_2]
            array[index_1] = new_item

    data = input()

print(', '.join([str(el) for el in array]))
