contract_duration = input()
contract_type = input()
mobile_internet = input()
months = int(input())

price_per_month = 0

if contract_duration == "one" and contract_type == "Small":
    price_per_month = 9.98
elif contract_duration == "one" and contract_type == "Middle":
    price_per_month = 18.99
elif contract_duration == "one" and contract_type == "Large":
    price_per_month = 25.98
elif contract_duration == "one" and contract_type == "ExtraLarge":
    price_per_month = 35.99

elif contract_duration == "two" and contract_type == "Small":
    price_per_month = 8.58
elif contract_duration == "two" and contract_type == "Middle":
    price_per_month = 17.09
elif contract_duration == "two" and contract_type == "Large":
    price_per_month = 23.59
elif contract_duration == "two" and contract_type == "ExtraLarge":
    price_per_month = 31.79


if mobile_internet == "yes" and price_per_month <= 10:
    price_per_month += 5.50
elif mobile_internet == "yes" and price_per_month <= 30:
    price_per_month += 4.35
elif mobile_internet == "yes" and price_per_month > 30:
    price_per_month += 3.85

total_tax = price_per_month * months

if contract_duration == "two":
    total_tax = total_tax - total_tax * 3.75 / 100

print(f"{total_tax:.2f} lv.")
