city = input()
package = input()
vip_discount = input()
days = int(input())

price_per_day = 0
total_price = 0

if days > 7:
    days -= 1

if (city == "Bansko" or city == "Borovets") and package == "withEquipment":
    price_per_day = 100
    if vip_discount == "yes":
        total_price = days * price_per_day * 0.90
    elif vip_discount == "no":
        total_price = days * price_per_day

elif (city == "Bansko" or city == "Borovets") and package == "noEquipment":
    price_per_day = 80
    if vip_discount == "yes":
        total_price = days * price_per_day * 0.95
    elif vip_discount == "no":
        total_price = days * price_per_day

elif (city == "Varna" or city == "Burgas") and package == "withBreakfast":
    price_per_day = 130
    if vip_discount == "yes":
        total_price = days * price_per_day * 0.88
    elif vip_discount == "no":
        total_price = days * price_per_day

elif (city == "Varna" or city == "Burgas") and package == "noBreakfast":
    price_per_day = 100
    if vip_discount == "yes":
        total_price = days * price_per_day * 0.93
    elif vip_discount == "no":
        total_price = days * price_per_day

else:
    print("Invalid input!")

if days < 1:
    print("Days must be positive number!")

if total_price > 0:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")





