import math

guests_number = int(input())
budget = int(input())

eastern_bread = math.ceil(guests_number / 3)
eggs = guests_number * 2

total_price = eggs * 0.45 + eastern_bread * 4

if total_price <= budget:
    left_money = budget - total_price
    print(f"Lyubo bought {eastern_bread} Easter bread and {eggs} eggs.")
    print(f"He has {left_money:.2f} lv. left.")
else:
    needed_money = total_price - budget
    print("Lyubo doesn't have enough money.")
    print(f"He needs {needed_money:.2f} lv. more.")
