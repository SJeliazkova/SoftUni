waiting_people = int(input())
wagons = input().split()

MAX_PEOPLE_IN_WAGON = 4

wagons = [int(el) for el in wagons]


for i in range(len(wagons)):
    while not wagons[i] == MAX_PEOPLE_IN_WAGON:
        if waiting_people > 0:
            wagons[i] += 1
            waiting_people -= 1
        else:
            break

taken_seats = sum(wagons)
max_seats = len(wagons) * MAX_PEOPLE_IN_WAGON

if taken_seats < max_seats:
    print("The lift has empty spots!")

elif taken_seats == max_seats and waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")

print(f"{' '.join([ str(el) for el in wagons ])}")

