n = int(input())

divided_2 = 0
divided_3 = 0
divided_4 = 0

for i in range(1, n+1):
    num_value = int(input())

    if num_value % 2 == 0:
        divided_2 += 1
    if num_value % 3 == 0:
        divided_3 += 1
    if num_value % 4 == 0:
        divided_4 += 1

divided_2_percent = divided_2 / n * 100
divided_3_percent = divided_3 / n * 100
divided_4_percent = divided_4 / n * 100

print(f"{divided_2_percent:.2f}%")
print(f"{divided_3_percent:.2f}%")
print(f"{divided_4_percent:.2f}%")