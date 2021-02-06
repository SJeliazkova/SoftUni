n = int(input())

chemical_elements = set()

for _ in range(n):
    line = input().split()
    for el in line:
        chemical_elements.add(el)

for el in chemical_elements:
    print(el)