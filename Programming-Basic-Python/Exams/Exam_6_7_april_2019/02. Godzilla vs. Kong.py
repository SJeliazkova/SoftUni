budget = float(input())
statists_cnt = int(input())
clothes_price_per_statist = float(input())

decor = budget * 0.10
clothes_price = statists_cnt * clothes_price_per_statist

if statists_cnt >= 150:
    clothes_price = clothes_price * 0.9

expenses = clothes_price + decor

if budget < expenses:
    money_need = expenses - budget
    print("Not enough money!")
    print(f"Wingard needs {money_need:.2f} leva more.")
else:
    money_left = budget - expenses
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")