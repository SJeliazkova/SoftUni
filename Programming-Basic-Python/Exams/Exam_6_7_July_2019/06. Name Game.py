player_name = input()

winner_name = ""
winner_score = 0

while player_name != "Stop":
    len_name = len(player_name)
    player_score = 0

    for i in range(0, len_name ):
        number = int(input())
        current_letter = ord(player_name[i])

        if current_letter == number:
            player_score += 10
        else:
            player_score += 2

    if player_score >= winner_score:
        winner_name = player_name
        winner_score = player_score


    player_name = input()

else:
    print(f"The winner is {winner_name} with {winner_score} points!")



