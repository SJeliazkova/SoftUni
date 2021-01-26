games_count = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for i in range(1, games_count + 1):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1

hearthstone_percent = hearthstone / games_count * 100
fornite_percent = fornite / games_count * 100
overwatch_percent = overwatch / games_count * 100
others_percent = others / games_count * 100

print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {others_percent:.2f}%")