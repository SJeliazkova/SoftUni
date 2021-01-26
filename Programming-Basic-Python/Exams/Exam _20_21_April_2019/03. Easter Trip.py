destination = input()
date = input()
nights = int(input())

night_price = 0

if destination == "France":
    if date == "21-23":
        night_price = 30
    elif date == "24-27":
        night_price = 35
    elif date == "28-31":
        night_price = 40
elif destination == "Italy":
    if date == "21-23":
        night_price = 28
    elif date == "24-27":
        night_price = 32
    elif date == "28-31":
        night_price = 39
elif destination == "Germany":
    if date == "21-23":
        night_price = 32
    elif date == "24-27":
        night_price = 37
    elif date == "28-31":
        night_price = 43

total_price = nights * night_price

print(f"Easter trip to {destination} : {total_price:.2f} leva.")
