first_game = input()
second_game = input()
third_game = input()

won = 0
lost = 0
drawn = 0

team_1_first_game = int(first_game[0])
team_2_first_game = int(first_game[2])

team_1_second_game = int(second_game[0])
team_2_second_game = int(second_game[2])

team_1_third_game = int(third_game[0])
team_2_third_game = int(third_game[2])

if team_1_first_game > team_2_first_game:
    won += 1
elif team_1_first_game == team_2_first_game:
    drawn += 1
else:
    lost += 1

if team_1_second_game > team_2_second_game:
    won += 1
elif team_1_second_game == team_2_second_game:
    drawn += 1
else:
    lost += 1

if team_1_third_game > team_2_third_game:
    won += 1
elif team_1_third_game == team_2_third_game:
    drawn += 1
else:
    lost += 1

print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn}")