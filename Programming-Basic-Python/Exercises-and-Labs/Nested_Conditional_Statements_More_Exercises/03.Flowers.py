number_of_chrysanthemums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
type_of_day = input()

price_of_chrysanthemums = 0
price_of_roses = 0
price_of_tulips = 0

if season == "Spring" or season == "Summer":
    price_of_chrysanthemums = 2
    price_of_roses = 4.1
    price_of_tulips = 2.50
elif season == "Autumn" or season == "Winter":
    price_of_chrysanthemums = 3.75
    price_of_roses = 4.50
    price_of_tulips = 4.15

flowers_price = price_of_chrysanthemums * number_of_chrysanthemums + \
                price_of_roses * number_of_roses + price_of_tulips * number_of_tulips
all_flowers = number_of_roses + number_of_tulips + number_of_chrysanthemums

if type_of_day == "Y":
    flowers_price = flowers_price * 1.15

if number_of_tulips > 7 and season == "Spring":
    flowers_price = flowers_price * 0.95

if number_of_roses >= 10 and season == "Winter":
    flowers_price = flowers_price * 0.90

if all_flowers > 20:
    flowers_price = flowers_price * 0.80

final_price = 2 + flowers_price

print(f"{final_price:.2f}")
