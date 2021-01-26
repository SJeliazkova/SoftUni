days = int(input())
room_type = input()
grade = input()

# цена на нощувката според типа стая
price_per_night = 0
percentage = 1    # когато нямаме отстъпка
# процентна отстъпка спрямо броя нощувки

if room_type == "room for one person":
    price_per_night = 18

elif room_type == "apartment":
    price_per_night = 25

    if days < 10:
        percentage = 0.7
    elif 10 <= days <= 15:
        percentage = 0.65
    elif days > 15:
        percentage = 0.5


elif room_type == "president apartment":
    price_per_night = 35

    if days < 10:
        percentage = 0.9
    elif 10 <= days <= 15:
        percentage = 0.85
    elif days > 15:
        percentage = 0.8

# броя на нощувките
nights = days - 1

# цена на нощувките
total_price = nights * price_per_night

# проспадане на отстъпката от цената
total_price = total_price * percentage

# да се приспаде отстъпка спрямо оценката
percentage_grade = 1
if grade == "positive":
    percentage_grade = 1.25
else:
    percentage_grade = 0.9

total_price = total_price * percentage_grade
print(f"{total_price:.2f}")


