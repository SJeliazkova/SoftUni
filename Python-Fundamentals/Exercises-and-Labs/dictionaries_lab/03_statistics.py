data = input()

food = {}

while not data == "statistics":
    product, quantity = data.split(": ")
    quantity = int(quantity)

    if product not in food:
        food[product] = 0
    food[product] += quantity

    data = input()

print("Products in stock:")
for product, quantity in food.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(food)}")
print(f"Total Quantity: {sum(food.values())}")