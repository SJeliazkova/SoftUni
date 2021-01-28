data = input().split(", ")

numbers = list(map(int, data))

evens_num_index = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]

print(evens_num_index)

