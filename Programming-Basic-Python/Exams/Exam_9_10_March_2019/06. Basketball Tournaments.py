tournament_name = input()

wins = 0
losts = 0
games = 0

while tournament_name != "End of tournaments":
    game_count = int(input())

    for game_num in range(1, game_count + 1):
        team_desi_score = int(input())
        team_2_score = int(input())

        if team_desi_score > team_2_score:
            wins += 1
            games += 1
            print(f"Game {game_num} of tournament {tournament_name}: win with {abs(team_desi_score - team_2_score)} points.")

        else:
            losts += 1
            games += 1
            print(f"Game {game_num} of tournament {tournament_name}: lost with {abs(team_2_score - team_desi_score)} points.")

    tournament_name = input()

else:
    wins_percent = wins / games * 100
    losts_percent = losts / games * 100

    print(f"{wins_percent:.2f}% matches win")
    print(f"{losts_percent:.2f}% matches lost")
