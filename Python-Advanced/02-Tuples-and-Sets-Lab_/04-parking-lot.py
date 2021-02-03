n = int(input())
parking_lot = set([ ])

for _ in range(n):
    command, plate = input().split(", ")

    if command == "IN":
        parking_lot.add(plate)
    else:
        parking_lot.remove(plate)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")