film_name = input()
package = input()
tickets_num = int(input())

tickets_price = 0

if film_name == "John Wick":
    if package == "Drink":
        tickets_price = tickets_num * 12
    elif package == "Popcorn":
        tickets_price = tickets_num * 15
    elif package == "Menu":
        tickets_price = tickets_num * 19

elif film_name == "Star Wars":
    if package == "Drink":
        tickets_price = tickets_num * 18
    elif package == "Popcorn":
        tickets_price = tickets_num * 25
    elif package == "Menu":
        tickets_price = tickets_num * 30

elif film_name == "Jumanji":
    if package == "Drink":
        tickets_price = tickets_num * 9
    elif package == "Popcorn":
        tickets_price = tickets_num * 11
    elif package == "Menu":
        tickets_price = tickets_num * 14

if film_name == "Star Wars" and tickets_num >= 4:
    if package == "Drink":
        tickets_price = tickets_num * 18 * 0.70
    elif package == "Popcorn":
        tickets_price = tickets_num * 25 * 0.70
    elif package == "Menu":
        tickets_price = tickets_num * 30 * 0.70

if film_name == "Jumanji" and tickets_num == 2:
    if package == "Drink":
        tickets_price = tickets_num * 9 * 0.85
    elif package == "Popcorn":
        tickets_price = tickets_num * 11 * 0.85
    elif package == "Menu":
        tickets_price = tickets_num * 14 * 0.85

print(f"Your bill is {tickets_price:.2f} leva.")


