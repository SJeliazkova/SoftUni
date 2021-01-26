bees = int(input())
bear_health = int(input())
bear_attack = int(input())

while bees >= 100:
    # мечката атакува първа
    bees -= bear_attack
    bees_attack = bees * 5
    # пчелите атакуват
    bear_health -= bees_attack

    if bear_health <= 0:
        print(f"Beehive won! Bees left {bees}.")
        break

else:
    if bees < 0:
        bees = 0
    else:
        bees = bees

    print(f"The bear stole the honey! Bees left {bees}.")



