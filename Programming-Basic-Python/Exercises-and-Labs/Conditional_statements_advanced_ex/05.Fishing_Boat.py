budget = float(input())
season = input()
number_of_fisherman = int(input())

rent = 0
# наем за кораб според сезона
if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

# отстъпка според броя на рибарите
if number_of_fisherman <= 6:
    rent = rent * 0.9
elif 7 <= number_of_fisherman <= 11:
    rent = rent * 0.85
else:
    rent = rent * 0.75

# допълнителна отстъпка
if number_of_fisherman % 2 == 0 and season != "Autumn":
    rent = rent * 0.95

# проверка дали бюджета е достатъчен
if budget >= rent:
    left_money = budget - rent
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    need_money = rent - budget
    print(f"Not enough money! You need {need_money:.2f} leva.")