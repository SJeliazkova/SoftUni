number_of_cago = int(input())

bus_price = 0
truck_price = 0
train_price = 0
bus_tonnage = 0
train_tonnage = 0
truck_tonnage = 0

for number in range(1, number_of_cago + 1):
    tonnage = int(input())

    if tonnage <= 3:
        bus_price += 200 * tonnage
        bus_tonnage += tonnage

    elif 4 <= tonnage <= 11:
        truck_price += 175 * tonnage
        truck_tonnage += tonnage

    elif tonnage >= 12:
        train_price += 120 * tonnage
        train_tonnage += tonnage

all_tonnage = bus_tonnage + truck_tonnage + train_tonnage
mid_price = (bus_price + train_price + truck_price) / all_tonnage

bus_percent = bus_tonnage / all_tonnage * 100
truck_percent = truck_tonnage / all_tonnage * 100
train_percent = train_tonnage / all_tonnage * 100

print(f"{mid_price:.2f}")
print(f"{bus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")