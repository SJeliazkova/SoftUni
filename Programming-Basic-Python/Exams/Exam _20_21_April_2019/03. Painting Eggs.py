egg_size = input()
color = input()
num_batch = int(input())

egg_price = 0

if egg_size == "Large":
    if color == "Red":
        egg_price = 16
    elif color == "Green":
        egg_price = 12
    elif color == "Yellow":
        egg_price = 9
elif egg_size == "Medium":
    if color == "Red":
        egg_price = 13
    elif color == "Green":
        egg_price = 9
    elif color == "Yellow":
        egg_price = 7
elif egg_size == "Small":
    if color == "Red":
        egg_price = 9
    elif color == "Green":
        egg_price = 8
    elif color == "Yellow":
        egg_price = 5

total_price = egg_price * num_batch
costs = total_price * 0.35
total = total_price - costs

print(f"{total:.2f} leva.")
