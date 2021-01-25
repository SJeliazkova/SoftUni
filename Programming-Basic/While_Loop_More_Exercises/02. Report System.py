expected_money = int(input())

cash_pay = 0
card_pay = 0
counter = 0
cash_counter = 0
card_counter = 0
collected_money = 0
money = 0

while collected_money < expected_money:
    command = input()

    if command == "End":
        print("Failed to collect required money for charity.")
        break
    else:
        counter += 1
        money = int(command)

    if counter % 2 == 0 and money > 10:
        card_counter += 1
        card_pay += money
        collected_money += money
        print("Product sold!")
    elif counter % 2 == 0 and money <= 10:
        print("Error in transaction!")
    elif counter % 2 != 0 and money > 100:
        print("Error in transaction!")
    elif counter % 2 != 0 and money <= 100:
        cash_counter += 1
        cash_pay += money
        collected_money += money
        print("Product sold!")


if collected_money >= expected_money:
    average_cash_pay = cash_pay / cash_counter
    average_card_pay = card_pay / card_counter
    print(f"Average CS: {average_cash_pay:.2f}")
    print(f"Average CC: {average_card_pay:.2f}")



