data = input()

price_dict = {}
quantity_dict = {}

while not data == "buy":
    product, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if product not in price_dict:
        price_dict[product] = price
        quantity_dict[product] = quantity
    else:
        price_dict[product] = price
        quantity_dict[product] += quantity

    data = input()

for product, price in price_dict.items():
    total_price = price * quantity_dict[product]
    print(f"{product} -> {total_price:.2f}")



