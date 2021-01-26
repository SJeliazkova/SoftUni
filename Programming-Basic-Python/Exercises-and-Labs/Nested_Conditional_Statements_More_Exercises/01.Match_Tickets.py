budget = float(input())
category = input()
number_of_people = int(input())

transport_price = 0
tickets_price = 0

if 1 <= number_of_people <= 4:
    transport_price = budget * 0.75
elif 5 <= number_of_people <= 9:
    transport_price = budget * 0.60
elif 10 <= number_of_people <= 24:
    transport_price = budget * 0.50
elif 25 <= number_of_people <= 49:
    transport_price = budget * 0.40
elif number_of_people >= 50:
    transport_price = budget * 0.25

left_money_for_tickets = budget - transport_price

if category == "VIP":
    tickets_price = number_of_people * 499.99
elif category == "Normal":
    tickets_price = number_of_people * 249.99

if left_money_for_tickets >= tickets_price:
    final_left_money = left_money_for_tickets - tickets_price
    print(f"Yes! You have {final_left_money:.2f} leva left.")
else:
    needed_money = tickets_price - left_money_for_tickets
    print(f"Not enough money! You need {needed_money:.2f} leva.")
