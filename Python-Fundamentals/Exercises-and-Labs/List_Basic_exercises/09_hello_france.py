collection = input().split("|")
budget = float(input())

new_prices = []
profit = 0

for item in collection:
    item_data = item.split("->")
    item_type = item_data[0]
    item_price = float(item_data[1])

    if item_type == "Clothes" and item_price > 50:
        continue
    elif item_type == "Shoes" and item_price > 35:
        continue
    elif item_type == "Accessories" and item_price > 20.5:
        continue

    if budget >= item_price:
        budget -= item_price
        new_prices.append(item_price * 1.40)
        profit += item_price * 0.40

for element in new_prices:
    print(f"{element:.2f} ", end="")

print()
print(f"Profit: {profit:.2f}")

money_for_travel = budget + sum(new_prices)
if money_for_travel >= 150:
    print("Hello, France!")
else:
    print("Time to go.")


