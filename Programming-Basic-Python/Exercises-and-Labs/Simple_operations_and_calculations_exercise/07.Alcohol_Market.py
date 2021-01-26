# вход всички променливи - реално число
# цена на ракията = цена на уискито / 2
# цена на виното = цена на ракията * 0.6
# цена на бирата = цена на ракията * 0.2
# обща цена = ....
# принт обща цена до 2 знак

whiskey_price = float(input())
beer_quantity = float(input())
wine_quantity = float(input())
rakia_quantity = float(input())
whiskey_quantity = float(input())

rakia_price = whiskey_price / 2
wine_price = rakia_price * 0.6
beer_price = rakia_price * 0.2

total_sum = whiskey_price * whiskey_quantity + rakia_price * rakia_quantity + wine_price * wine_quantity + beer_price * beer_quantity
print(f"{total_sum:.2f}")