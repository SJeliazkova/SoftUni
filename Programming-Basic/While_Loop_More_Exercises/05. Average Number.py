num = int(input())

sum = 0

for num in range ( 1, num + 1):
    value = int(input())
    sum += value

average = sum / num
print(f"{average:.2f}")