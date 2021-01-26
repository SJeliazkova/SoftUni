first_player_name = input()
second_player_name = input()

first_player_score = 0
second_player_score = 0

command = input()

while command != "End of game":
    first_player_card = int(command)
    second_player_card = int(input())
    if first_player_card > second_player_card:
        diff = first_player_card - second_player_card
        first_player_score += diff
    elif second_player_card > first_player_card:
        diff = second_player_card - first_player_card
        second_player_score += diff
    elif first_player_card == second_player_card:
        first_player_sec_card = int(input())
        second_player_sec_card = int(input())
        if first_player_sec_card > second_player_sec_card:
            print("Number wars!")
            print(f"{first_player_name} is winner with {first_player_score} points")
        else:
            print("Number wars!")
            print(f"{second_player_name} is winner with {second_player_score} points")
        break

    command = input()


else:
    print(f"{first_player_name} has {first_player_score} points")
    print(f"{second_player_name} has {second_player_score} points")





