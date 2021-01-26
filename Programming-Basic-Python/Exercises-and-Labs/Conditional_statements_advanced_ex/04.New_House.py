type_of_flowers = input()
number_of_flowers = int(input())
budget = float(input())

total_price = 0

if type_of_flowers == "Roses":
    total_price = number_of_flowers * 5
    if number_of_flowers > 80:
        total_price = total_price * 0.9

elif type_of_flowers == "Dahlias":
    total_price = number_of_flowers * 3.80
    if number_of_flowers > 90:
        total_price = total_price * 0.85

elif type_of_flowers == "Tulips":
    total_price = number_of_flowers * 2.80
    if number_of_flowers > 80:
        total_price = total_price * 0.85


elif type_of_flowers == "Narcissus":
    total_price = number_of_flowers * 3
    if number_of_flowers < 120:
        total_price = total_price * 1.15

elif type_of_flowers == "Gladiolus":
    total_price = number_of_flowers * 2.50
    if number_of_flowers < 80:
        total_price = total_price * 1.20

if budget >= total_price:
    money_left =  budget - total_price
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {money_left:.2f} leva left.")
else:
    money_need = total_price - budget
    print(f"Not enough money, you need {money_need:.2f} leva more.")