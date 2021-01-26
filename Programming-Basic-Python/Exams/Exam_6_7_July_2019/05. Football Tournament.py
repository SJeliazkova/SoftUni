team_name = input()
games_count = int(input())

w_game = 0
d_game = 0
l_game = 0
total_score = 0

if games_count == 0:
    print(f"{team_name} hasn't played any games during this season.")

elif games_count != 0:

    for i in range(1, games_count + 1):
        result = input()
        if result == "W":
            w_game += 1
            total_score += 3
        elif result == "D":
            d_game += 1
            total_score += 1
        elif result == "L":
            l_game += 1

    win_rate = w_game / games_count * 100

    print(f"{team_name} has won {total_score} points during this season.")
    print("Total stats:")
    print(f"## W: {w_game}")
    print(f"## D: {d_game}")
    print(f"## L: {l_game}")
    print(f"Win rate: {win_rate:.2f}%")






