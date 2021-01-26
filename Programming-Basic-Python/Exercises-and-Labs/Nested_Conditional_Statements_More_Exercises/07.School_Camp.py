season = input()
type_of_group = input()
number_of_students = int(input())
number_of_nights = int(input())

price = 0
sport = ""

if season == "Winter":
    if type_of_group == "girls":
        sport = "Gymnastics"
        price = number_of_students * number_of_nights * 9.60
    elif type_of_group == "boys":
        sport = "Judo"
        price = number_of_students * number_of_nights * 9.60
    elif type_of_group == "mixed":
        sport = "Ski"
        price = number_of_students * number_of_nights * 10

if season == "Spring":
    if type_of_group == "girls":
        sport = "Athletics"
        price = number_of_students * number_of_nights * 7.20
    elif type_of_group == "boys":
        sport = "Tennis"
        price = number_of_students * number_of_nights * 7.20
    elif type_of_group == "mixed":
        sport = "Cycling"
        price = number_of_students * number_of_nights * 9.50

if season == "Summer":
    if type_of_group == "girls":
        sport = "Volleyball"
        price = number_of_students * number_of_nights * 15
    elif type_of_group == "boys":
        sport = "Football"
        price = number_of_students * number_of_nights * 15
    elif type_of_group == "mixed":
        sport = "Swimming"
        price = number_of_students * number_of_nights * 20

if number_of_students >= 50:
    price = price * 0.50
elif 20 <= number_of_students < 50:
    price = price * 0.85
elif 10 <= number_of_students < 20:
    price = price * 0.95

print(f"{sport} {price:.2f} lv.")