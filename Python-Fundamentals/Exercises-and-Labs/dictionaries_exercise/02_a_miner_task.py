data = input()

resources = {}

while not data == "stop":
    material = data
    quantity = int(input())

    if material not in resources:
        resources[material] = 0
    resources[material] += quantity

    data = input()

for key, value in resources.items():
    print(f"{key} -> {value}")