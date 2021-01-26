budget = float(input())
needed_fuel = float(input())
day = input()

fuel_price = needed_fuel * 2.10
trip_price = 100 + fuel_price

if day == "Saturday":
    trip_price = trip_price * 0.90
elif day == "Sunday":
    trip_price = trip_price * 0.80

if trip_price <= budget:
    left_money = budget - trip_price
    print(f"Safari time! Money left: {left_money:.2f} lv.")
else:
    needed_money = trip_price - budget
    print(f"Not enough money! Money needed: {needed_money:.2f} lv.")