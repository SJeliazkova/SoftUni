budget = float(input())
number_of_nights = int(input())
night_price = float(input())
other_cost_percent = int(input())

if number_of_nights > 7:
    night_price = night_price * 0.95

trip_price = number_of_nights * night_price + budget * other_cost_percent / 100

if trip_price <= budget:
    left_money = budget - trip_price
    print(f"Ivanovi will be left with {left_money:.2f} leva after vacation.")

else:
    needed_money = trip_price - budget
    print(f"{needed_money:.2f} leva needed.")