n = int(input())

numbers = []
filtered_num = []

for i in range(n):
    current_num = int(input())
    numbers.append(current_num)

command = input()

if command == "even":
    for num in numbers:
        if num % 2 == 0:
            filtered_num.append(num)

if command == "odd":
    for num in numbers:
        if num % 2 != 0:
            filtered_num.append(num)

if command == "negative":
    for num in numbers:
        if num < 0:
            filtered_num.append(num)

if command == "positive":
    for num in numbers:
        if num >= 0:
            filtered_num.append(num)

print(filtered_num)


