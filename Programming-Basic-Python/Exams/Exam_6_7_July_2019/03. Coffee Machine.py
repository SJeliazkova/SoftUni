drink_type = input()
sugar = input()
number_of_drinks = int(input())

drink_price = 0

if drink_type == "Espresso":
    if sugar == "Without":
        drink_price = number_of_drinks * 0.90 * 0.65
    elif sugar == "Normal":
        drink_price = number_of_drinks * 1
    elif sugar == "Extra":
        drink_price = number_of_drinks * 1.20

elif drink_type == "Cappuccino":
    if sugar == "Without":
        drink_price = number_of_drinks * 1 * 0.65
    elif sugar == "Normal":
        drink_price = number_of_drinks * 1.20
    elif sugar == "Extra":
        drink_price = number_of_drinks * 1.60

elif drink_type == "Tea":
    if sugar == "Without":
        drink_price = number_of_drinks * 0.50 * 0.65
    elif sugar == "Normal":
        drink_price = number_of_drinks * 0.60
    elif sugar == "Extra":
        drink_price = number_of_drinks * 0.70

if drink_type == "Espresso" and number_of_drinks >= 5:
    if sugar == "Without":
        drink_price = number_of_drinks * 0.90 * 0.65 * 0.75
    elif sugar == "Normal":
        drink_price = number_of_drinks * 1 * 0.75
    elif sugar == "Extra":
        drink_price = number_of_drinks * 1.20 * 0.75

if drink_price > 15:
    drink_price = drink_price * 0.80

print(f"You bought {number_of_drinks} cups of {drink_type} for {drink_price:.2f} lv.")
