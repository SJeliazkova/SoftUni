numbers_as_str = input().split(", ")

numbers = list(map(int, numbers_as_str))
counter = numbers.count(0)

while 0 in numbers: numbers.remove(0)

for n in range(counter):
    numbers.append(0)

print(numbers)