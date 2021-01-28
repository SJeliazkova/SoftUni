numbers = list(map(int, input().split()))

average = sum(numbers) / len(numbers)

greater_numbers = []
result = []

for num in numbers:
    if num > average:
        greater_numbers.append(num)

greater_numbers.sort(reverse=True)
counter = 0

for i in range(len(greater_numbers)):
    result.append(greater_numbers[i])
    counter += 1
    if counter == 5:
        break

if len(result) != 0:
    print(' '.join([str(el) for el in result]))
else:
    print("No")