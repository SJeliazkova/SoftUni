distance = int(input())
day_or_night = input()

total_price_taxi = 0
total_price_bus = 0
total_price_train = 0

if distance < 20:
    if day_or_night == "day":
        total_price_taxi = distance * 0.79 + 0.70
    else:
        total_price_taxi = distance * 0.90 + 0.70

    print(f"{total_price_taxi:.2f}")

elif distance >= 100:
    if day_or_night == "day":
        total_price_taxi = distance * 0.79 + 0.70
    else:
        total_price_taxi = distance * 0.90 + 0.70

    total_price_bus = distance * 0.09
    total_price_train = distance * 0.06

    if total_price_taxi < total_price_bus:
        if total_price_taxi < total_price_train:
            print(f"{total_price_taxi:.2f}")
        else:
            print(f"{total_price_train:.2f}")
    else:
       if total_price_bus < total_price_train:
           print(f"{total_price_bus:.2f}")
       else:
           print(f"{total_price_train:.2f}")

elif distance >= 20:
    if day_or_night == "day":
        total_price_taxi = distance * 0.79 + 0.70
    else:
        total_price_taxi = distance * 0.90 + 0.70

    total_price_bus = distance * 0.09

    if total_price_taxi < total_price_bus:
        print(f"{total_price_taxi:.2f}")
    else:
        print(f"{total_price_bus:.2f}")

