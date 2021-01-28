import math

numbers = list(map(int, input().split(", ")))

for n in range(1, math.ceil(max(numbers) / 10 + 1)):
    result = [numbers[index] for index in range(len(numbers)) if numbers[index] in range(n * 10 - 10 + 1, n * 10 + 1)]

    print(f"Group of {n*10}'s: {result}")