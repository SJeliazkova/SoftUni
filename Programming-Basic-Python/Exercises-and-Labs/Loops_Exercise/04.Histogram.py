n = int(input())

group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0

for i in range( 1, n + 1):
    value = int(input())
    if value < 200:
        group_1 += 1
    elif 200 <= value <= 399:
        group_2 += 1
    elif 400 <= value <= 599:
        group_3 += 1
    elif 600 <= value <= 799:
        group_4 += 1
    elif value >= 800:
        group_5 += 1

percent1 = group_1 / n * 100
percent2 = group_2 / n * 100
percent3 = group_3 / n * 100
percent4 = group_4 / n * 100
percent5 = group_5 / n * 100

print(f"{percent1:.2f}%")
print(f"{percent2:.2f}%")
print(f"{percent3:.2f}%")
print(f"{percent4:.2f}%")
print(f"{percent5:.2f}%")


