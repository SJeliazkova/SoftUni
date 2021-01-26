n = int(input())

group_1 = 0
group_2 = 0
group_3 = 0


for i in range( 1, n + 1):
    value = int(input())
    if value % 2 == 0:
        group_1 += 1
    if value % 3 == 0:
        group_2 += 1
    if value % 4 == 0:
        group_3 += 1

percent1 = group_1 / n * 100
percent2 = group_2 / n * 100
percent3 = group_3 / n * 100


print(f"{percent1:.2f}%")
print(f"{percent2:.2f}%")
print(f"{percent3:.2f}%")


