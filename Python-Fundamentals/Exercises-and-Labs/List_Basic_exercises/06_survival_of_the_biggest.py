numbers_str = input().split()
n = int(input())

numbers = []

for num in numbers_str:
    current_num = int(num)
    numbers.append(current_num)


for i in range(n):
    min_number = 999999999999999999999999
    for num in numbers:
        current_num = num
        if current_num < min_number:
            min_number = current_num

    numbers.remove(min_number)


print(numbers)
