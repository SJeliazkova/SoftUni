guests_number = int(input())
tax_per_person = float(input())
budget = float(input())


if 10 <= guests_number <= 15:
    tax_per_person = tax_per_person * 0.85
elif 15 < guests_number <= 20:
    tax_per_person = tax_per_person * 0.80
elif guests_number > 20:
    tax_per_person = tax_per_person * 0.75

guests_tax = guests_number * tax_per_person
cake_price = budget * 0.10
total_price = guests_tax + cake_price

if total_price <= budget:
    left_money = budget - total_price
    print(f"It is party time! {left_money:.2f} leva left.")
else:
    needed_money = total_price - budget
    print(f"No party! {needed_money:.2f} leva needed.")

