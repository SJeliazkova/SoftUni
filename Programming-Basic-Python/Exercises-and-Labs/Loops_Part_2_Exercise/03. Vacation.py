needed_money = float(input())
owned_money = float(input())

days_counter = 0
spending_days_counter = 0

while owned_money < needed_money and spending_days_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1

    if command == 'save':
        owned_money += money
        spending_days_counter = 0

    elif command == 'spend':
        owned_money -= money
        spending_days_counter += 1
        if owned_money < 0:
            owned_money = 0


if spending_days_counter == 5:
    print(f"You can't save the money.")
    print(days_counter)
else:
    print(f"You saved the money for {days_counter} days.")



