import sys
films_count = int(input())

max_rating = -sys.maxsize
min_rating = sys.maxsize
highest_rating_film = ""
lowest_rating_film = ""
all_rating = 0

for i in range(1, films_count + 1):
    film_name = input()
    film_rating = float(input())

    if film_rating > max_rating:
        max_rating = film_rating
        highest_rating_film = f"{film_name}"

    if film_rating < min_rating:
        min_rating = film_rating
        lowest_rating_film = f"{film_name}"

    all_rating += film_rating

average = all_rating / films_count

print(f"{highest_rating_film} is with highest rating: {max_rating:.1f}")
print(f"{lowest_rating_film} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average:.1f}")

