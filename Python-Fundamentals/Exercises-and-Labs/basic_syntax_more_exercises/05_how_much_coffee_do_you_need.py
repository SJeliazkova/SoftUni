command = input()

LOWER_EVENTS = ["coding", "dog", "cat", "movie"]
UPPER_EVENTS = ["CODING", "DOG", "CAT", "MOVIE"]

counter = 0
is_exhausted = False

while command != "END":
    if command in LOWER_EVENTS:
        counter += 1

    elif command in UPPER_EVENTS:
        counter += 2

    if counter > 5:
        print('You need extra sleep')
        is_exhausted = True
        break

    command = input()


if not is_exhausted:
    print(counter)




