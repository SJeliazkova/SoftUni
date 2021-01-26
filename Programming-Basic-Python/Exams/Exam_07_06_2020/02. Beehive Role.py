intellect = int(input())
power = int(input())
gender = input()

beehive_role = ""

check_queen = intellect >= 80 and power >= 80 and gender == "female"

if check_queen:
    beehive_role = "Queen Bee"
elif intellect >= 80:
    beehive_role = "Repairing Bee"
elif intellect >= 60:
    beehive_role = "Cleaning Bee"
elif power >= 80 and gender == "male":
    beehive_role = "Drone Bee"
elif power >= 60:
    beehive_role = "Guard Bee"
else:
    beehive_role = "Worker Bee"

print(beehive_role)