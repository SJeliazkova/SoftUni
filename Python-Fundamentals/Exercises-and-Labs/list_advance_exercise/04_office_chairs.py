rooms = int(input())

left_chair = []
needed_chairs = False

for room in range(1, rooms+1):
    data = input().split()
    chairs = data[0].count("X")
    taken_place = int(data[1])

    if chairs > taken_place:
        free_chair = chairs - taken_place
        left_chair.append(free_chair)
    elif chairs < taken_place:
        needed_chairs = True
        needed_chair = taken_place - chairs
        print(f"{needed_chair} more chairs needed in room {room}")

total_free_chairs = sum(left_chair)

if not needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")