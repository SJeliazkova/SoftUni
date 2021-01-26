budget = float(input())

products = 0
total_price = 0
needed_money = 0
counter = 0

command = input()

while command != "Stop":
    counter += 1
    product_name = command
    product_price = float(input())

    if counter % 3 == 0:
        product_price = product_price / 2

    if product_price <= budget:
        budget -= product_price
        total_price += product_price
        products += 1
    else:
        needed_money = product_price - budget
        print("You don't have enough money!")
        print(f"You need {needed_money:.2f} leva!")
        break

    command = input()

else:
    print(f"You bought {products} products for {total_price:.2f} leva.")

