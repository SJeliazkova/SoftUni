#променлива за кв.метри които ще се озеленяват
#изчисляване на необходимите средства (кв.м * 7.61 лв.)
#изчисляване на отстъпката 18%
#изчисляване на крайната стойност, с начислена отстъпка

square_meters_for_greening = float(input())

price = square_meters_for_greening * 7.61
discount = price * 0.18
total_price = price - discount
print(f"The final price is: {total_price:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")