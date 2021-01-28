working_day = input().split("|")

current_energy = 100
coins = 100
gain_energy = 0
is_bankrupt = False


for el in working_day:
    item = el.split("-")
    event_ingredient = item[0]
    value = int(item[1])

    if event_ingredient == "rest":
        current_energy += value
        gain_energy = value
        if current_energy > 100:
            current_energy = 100
            gain_energy = 0

        print(f"You gained {gain_energy} energy.")
        print(f"Current energy: {current_energy}.")

    elif event_ingredient == "order":
        if current_energy >= 30:
            current_energy -= 30
            coins += value
            print(f"You earned {value} coins.")

        else:
            current_energy += 50
            print("You had to rest!")
            continue

    else:
        if coins > value:
            coins -= value
            print(f"You bought {event_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_ingredient}.")
            is_bankrupt = True
            break

if is_bankrupt == False:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")





