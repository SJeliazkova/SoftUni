film_name = input()
hall_type = input()
tickets_count = int(input())

tickets_price = 0

if film_name == "A Star Is Born" and hall_type == "normal":
    tickets_price = 7.50
elif film_name == "A Star Is Born" and hall_type == "luxury":
    tickets_price = 10.50
elif film_name == "A Star Is Born" and hall_type == "ultra luxury":
    tickets_price = 13.50

elif film_name == "Bohemian Rhapsody" and hall_type == "normal":
    tickets_price = 7.35
elif film_name == "Bohemian Rhapsody" and hall_type == "luxury":
    tickets_price = 9.45
elif film_name == "Bohemian Rhapsody" and hall_type == "ultra luxury":
    tickets_price = 12.75

elif film_name == "Green Book" and hall_type == "normal":
    tickets_price = 8.15
elif film_name == "Green Book" and hall_type == "luxury":
    tickets_price = 10.25
elif film_name == "Green Book" and hall_type == "ultra luxury":
    tickets_price = 13.25

elif film_name == "The Favourite" and hall_type == "normal":
    tickets_price = 8.75
elif film_name == "The Favourite" and hall_type == "luxury":
    tickets_price = 11.55
elif film_name == "The Favourite" and hall_type == "ultra luxury":
    tickets_price = 13.95

total_price = tickets_price * tickets_count

print(f"{film_name} -> {total_price:.2f} lv.")
