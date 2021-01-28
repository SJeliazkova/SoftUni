data = input().split()

products = {}

for index in range(0, len(data), 2):
    food = data[index]
    value = int(data[index + 1])

    products[food] = value

print(products)
