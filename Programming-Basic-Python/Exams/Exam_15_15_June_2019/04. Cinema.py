free_seats = int(input())

profits = 0
num_of_people = 0
tickets_price = 0

command = input()
while command != "Movie time!":

    num_of_people = int(command)

    if num_of_people > free_seats:
        print("The cinema is full.")
        break

    tickets_price = 5 * num_of_people
    free_seats -= num_of_people


    if num_of_people % 3 == 0:
        tickets_price = tickets_price - 5
        profits += tickets_price
    else:
        profits += tickets_price

    command = input()

else:
    print(f"There are {free_seats} seats left in the cinema.")

print(f"Cinema income - {profits} lv.")
