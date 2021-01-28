command = input()

total_price_without_tax = 0

while not (command == "special" or command == "regular"):
    price = float(command)
    if price <= 0:
        print("Invalid price!")
    else:
        total_price_without_tax += price

    command = input()

tax = total_price_without_tax * 0.2
total_price = total_price_without_tax + tax

if command == "special":
    total_price = total_price * 0.90

if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")




