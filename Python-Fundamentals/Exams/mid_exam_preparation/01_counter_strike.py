energy = int(input())
command = input()

wins = 0
is_alive = True

while command != "End of battle" or is_alive == False:
    distance = int(command)

    if energy >= distance:
        energy -= distance
        wins += 1
    else:
        print(f"Not enough energy! Game ends with {wins} won battles"
              f" and {energy} energy")
        is_alive = False
        break

    if wins % 3 == 0:
        energy += wins

    command = input()

if is_alive:
    print(f"Won battles: {wins}. Energy left: {energy}" )
