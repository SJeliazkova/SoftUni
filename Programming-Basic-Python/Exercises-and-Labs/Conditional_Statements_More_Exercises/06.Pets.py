import math

days = int(input())
food_kg = int(input())
food_for_dog_kg = float(input())
food_for_cat_kg = float(input())
food_for_turtle_g = float(input())

total_food_for_dog = days * food_for_dog_kg
total_food_for_cat = days * food_for_cat_kg
total_food_for_turtle = days * food_for_turtle_g / 1000
total_food = total_food_for_cat + total_food_for_dog + total_food_for_turtle

if total_food <= food_kg:
    left_food = food_kg - total_food
    print(f"{format(math.floor(left_food))} kilos of food left.")
else:
    needed_food = total_food - food_kg
    print(f"{format(math.ceil(needed_food))} more kilos of food are needed.")