capacity = int(input())
fans = int(input())

sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0

for i in range(1, fans + 1):
    sector = input()

    if sector == "A":
        sector_A += 1
    elif sector == "B":
        sector_B += 1
    elif sector == "V":
        sector_V += 1
    elif sector == "G":
        sector_G += 1

sector_A_percent = sector_A / fans * 100
sector_B_percent = sector_B / fans * 100
sector_V_percent = sector_V / fans * 100
sector_G_percent = sector_G / fans * 100
all_fans_percent = fans / capacity * 100

print(f"{sector_A_percent:.2f}%")
print(f"{sector_B_percent:.2f}%")
print(f"{sector_V_percent:.2f}%")
print(f"{sector_G_percent:.2f}%")
print(f"{all_fans_percent:.2f}%")


