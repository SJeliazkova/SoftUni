budget = float(input())
number_of_series = int(input())

total_sum = 0

for num in range(1, number_of_series + 1):
    series_name = input()
    series_price = float(input())

    if series_name == "Thrones":
        series_price = series_price * 0.50
    elif series_name == "Lucifer":
        series_price = series_price * 0.60
    elif series_name == "Protector":
        series_price = series_price * 0.70
    elif series_name == "TotalDrama":
        series_price = series_price * 0.80
    elif series_name == "Area":
        series_price = series_price * 0.90

    total_sum += series_price

if budget >= total_sum:
    left_money = budget - total_sum
    print(f"You bought all the series and left with {left_money:.2f} lv.")

else:
    needed_money = total_sum - budget
    print(f"You need {needed_money:.2f} lv. more to buy the series!")



