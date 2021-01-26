budget = float(input())
destination = input()
season = input()
days = int(input())

price_per_day = 0

if destination == "Dubai" and season == "Winter":
    price_per_day = 45000
elif destination == "Dubai" and season == "Summer":
    price_per_day = 40000
elif destination == "Sofia" and season == "Winter":
    price_per_day = 17000
elif destination == "Sofia" and season == "Summer":
    price_per_day = 12500
elif destination == "London" and season == "Winter":
    price_per_day = 24000
elif destination == "London" and season == "Summer":
    price_per_day = 20250

total_price = days * price_per_day

if destination == "Dubai":
    total_price = total_price * 0.70
if destination == "Sofia":
    total_price = total_price * 1.25

if budget >= total_price:
    left_money = budget - total_price
    print(f"The budget for the movie is enough! We have {left_money:.2f} leva left!")
else:
    needed_money = total_price - budget
    print(f"The director needs {needed_money:.2f} leva more!")