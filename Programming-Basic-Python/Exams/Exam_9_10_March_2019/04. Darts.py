player_name = input()

start_score = 301
win_score = 0
shots = 0
unsuccessful_shots = 0

while start_score > 0:
    command = input()
    if command == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break
    else:
        score = int(input())
        if command == "Single":
            win_score = score
        elif command == "Double":
            win_score = score * 2
        elif command == "Triple":
            win_score = score * 3

        if win_score > start_score:
            unsuccessful_shots += 1
        else:
            start_score -= win_score
            shots += 1

if start_score == 0:
    print(f"{player_name} won the leg with {shots} shots.")


