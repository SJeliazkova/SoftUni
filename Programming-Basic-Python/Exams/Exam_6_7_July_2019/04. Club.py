expected_profit = float(input())

collected_money = 0

while collected_money < expected_profit:
    command = input()

    if command == "Party!":
        needed_money = expected_profit - collected_money
        print(f"We need {needed_money:.2f} leva more.")
        print(f"Club income - {collected_money:.2f} leva.")
        break
    else:
        number_of_cocktails = int(input())
        cocktail_price = len(command)
        order_value = cocktail_price * number_of_cocktails
        if order_value % 2 != 0:
            order_value = order_value * 0.75

        collected_money += order_value

if collected_money >= expected_profit:
    print("Target acquired.")
    print(f"Club income - {collected_money:.2f} leva.")