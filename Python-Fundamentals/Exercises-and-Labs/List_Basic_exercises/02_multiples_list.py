factor = int(input())
counts = int(input())

elements = []

for num in range(1, counts + 1):
    current_num = num * factor
    elements.append(current_num)

print(elements)
