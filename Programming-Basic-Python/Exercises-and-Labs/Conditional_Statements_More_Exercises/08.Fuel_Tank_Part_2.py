type_fuel = input()
quantity_fuel = float(input())
discount_card = input()

price_fuel = 0
total_price = 0

if type_fuel == "Gas":
    price_fuel = 0.93
    if discount_card == "Yes":
        price_fuel = price_fuel - 0.08
    else:
        price_fuel = 0.93

    if 20 <= quantity_fuel <= 25:
        total_price = quantity_fuel * price_fuel * 0.92
    elif quantity_fuel > 25:
        total_price = quantity_fuel * price_fuel * 0.90
    else:
        total_price = quantity_fuel * price_fuel

if type_fuel == "Gasoline":
    price_fuel = 2.22
    if discount_card == "Yes":
        price_fuel = price_fuel - 0.18
    else:
        price_fuel = 2.22

    if 20 <= quantity_fuel <= 25:
        total_price = quantity_fuel * price_fuel * 0.92
    elif quantity_fuel > 25:
        total_price = quantity_fuel * price_fuel * 0.90
    else:
        total_price = price_fuel * quantity_fuel

if type_fuel == "Diesel":
    price_fuel = 2.33
    if discount_card == "Yes":
        price_fuel = price_fuel - 0.12
    else:
        price_fuel = 2.33

    if 20 <= quantity_fuel <= 25:
        total_price = quantity_fuel * price_fuel * 0.92
    elif quantity_fuel > 25:
        total_price = quantity_fuel * price_fuel * 0.90
    else:
        total_price = quantity_fuel * price_fuel

print(f"{total_price:.2f} lv.")


