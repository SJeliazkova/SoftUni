import math

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
present_price = float(input())

sum = magnolias * 3.25 + hyacinths * 4 + roses * 3.5 + cactus * 8
total_sum = sum * 0.95

if total_sum >= present_price:
    left_money = total_sum - present_price
    print(f"She is left with {format(math.floor(left_money))} leva.")
else:
    needed_money = present_price - total_sum
    print(f"She will have to borrow {format(math.ceil(needed_money))} leva.")