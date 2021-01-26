budget = float(input())
season = input()

destination = ""
type_of_journey = ""
sum = 0

#1 определяне на дестинацията спрямо бюджета
#2 определяне на типа почивка спрямо сезона
#3 определяне на бюджета според сезона

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_journey = "Camp"
        sum = 0.3 * budget
    elif season == "winter":
        type_of_journey = "Hotel"
        sum = 0.7 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_journey = "Camp"
        sum = 0.4 * budget
    elif season == "winter":
        type_of_journey = "Hotel"
        sum = 0.8 * budget
elif budget > 1000:
    destination = "Europe"
    type_of_journey = "Hotel"
    sum = 0.9 * budget

print(f"Somewhere in {destination}")
print(f"{type_of_journey} - {sum:.2f}")
