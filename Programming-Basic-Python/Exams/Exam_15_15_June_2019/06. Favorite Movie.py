

movie_name = input()

movie_counter = 0
the_best_movie_name = " "
tbm_points = 0

while movie_name != "STOP" :
    movie_counter += 1
    movie_points = 0
    points = 0

    if movie_counter == 7:
        print("The limit is reached.")
        print(f"The best movie for you is {the_best_movie_name} with {tbm_points} ASCII sum.")
        break

    for char in movie_name:
        sign_value = ord(char)

        if 'a' <= char <= 'z':
            points = sign_value - (2 * len(movie_name))
            movie_points += points
        elif 'A' <= char <= 'Z':
            points = sign_value - len(movie_name)
            movie_points += points
        else:
            points = sign_value
            movie_points += sign_value

    if movie_points > tbm_points:
        tbm_points = movie_points
        the_best_movie_name = movie_name

    movie_name = input()

else:
    print(f"The best movie for you is {the_best_movie_name} with {tbm_points} ASCII sum.")