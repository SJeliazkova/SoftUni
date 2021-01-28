dungeons_rooms = input().split("|")

health = 100
bitcoins = 0
room_counter = 0

for el in dungeons_rooms:
    command = el.split()[0]
    points = int(el.split()[1])
    room_counter += 1

    if command == "potion":
        health += points
        if health >= 100:
            healed = points - (health - 100)
            health = 100
        else:
            healed = points

        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += points
        print(f"You found {points} bitcoins.")

    else:
        monster = command
        health -= points

        if health <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_counter}")
            exit(0)
        else:
            print(f"You slayed {monster}.")

print(f"You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")