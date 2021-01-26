month = input()
number_of_nights = int(input())

total_price_studio = 0
total_price_apartment = 0

if month == "May" or month == "October":
    total_price_studio = number_of_nights * 50
    total_price_apartment = number_of_nights * 65

    if number_of_nights > 7 and number_of_nights <= 14:
        total_price_studio = total_price_studio * 0.95
    elif number_of_nights > 14:
        total_price_studio = total_price_studio * 0.7
        total_price_apartment = total_price_apartment * 0.9

elif month == "June" or month == "September":
    total_price_studio = number_of_nights * 75.2
    total_price_apartment = number_of_nights * 68.7

    if number_of_nights > 14:
        total_price_studio = total_price_studio * 0.80
        total_price_apartment = total_price_apartment * 0.90

elif month == "July" or month == "August":
    total_price_studio = number_of_nights * 76
    total_price_apartment = number_of_nights * 77

    if number_of_nights > 14:
        total_price_apartment = total_price_apartment * 0.90

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")