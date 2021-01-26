film_name = input()
days = int(input())
tickets_count = int(input())
tickets_price = float(input())
percent_for_cinema = int(input())

sum = days * tickets_count * tickets_price
money_for_cinema = sum * percent_for_cinema / 100
total_profit = sum - money_for_cinema

print(f"The profit from the movie {film_name} is {total_profit:.2f} lv.")