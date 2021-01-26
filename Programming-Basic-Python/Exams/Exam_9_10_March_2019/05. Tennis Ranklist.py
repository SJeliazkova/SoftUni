import  math
tournaments = int(input())
start_points = int(input())

points = start_points
wins = 0

for num in range(1, tournaments + 1):
    stage = input()

    if stage == "W":
        points += 2000
        wins += 1
    elif stage == "F":
        points += 1200
    elif stage == "SF":
        points += 720

average_points = (points - start_points) / tournaments
wins_percent = wins / tournaments * 100

print(f"Final points: {math.floor(points)}")
print(f"Average points: {math.floor(average_points)}")
print(f"{wins_percent:.2f}%")
