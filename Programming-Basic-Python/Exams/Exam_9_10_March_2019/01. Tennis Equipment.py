import math
tennis_racket_price = float(input())
tennis_racket_num = int(input())
sneakers_num = int(input())

sneakers_price = tennis_racket_price / 6
sum = sneakers_num * sneakers_price + tennis_racket_price * tennis_racket_num
other_costs = sum * 0.20

total_cost = sum + other_costs
djokovic_paid = total_cost / 8
sponsors_paid = total_cost - djokovic_paid

print(f"Price to be paid by Djokovic {math.floor(djokovic_paid)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_paid)}")