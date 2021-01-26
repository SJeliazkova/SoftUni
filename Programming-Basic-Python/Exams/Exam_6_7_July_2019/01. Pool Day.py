import math

people = int(input())
tax = float(input())
deck_chair_price = float(input())
umbrella_price = float(input())

all_tax = people * tax
deck_chair_total_price = math.ceil(people * 0.75) * deck_chair_price
umbrella_total_price = math.ceil(people / 2) * umbrella_price

total_sum = all_tax + deck_chair_total_price + umbrella_total_price

print(f"{total_sum:.2f} lv.")