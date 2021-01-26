months = int(input())

electricity_bill = 0
water_bill = 0
interner_bill = 0
other_bill = 0
all_bills = 0

for i in range(1, months+1):
    electricity = float(input())

    electricity_bill += electricity
    water_bill += 20
    interner_bill += 15
    other_bill += (electricity + 20 + 15) * 1.2

average = (electricity_bill + water_bill + interner_bill + other_bill) / months

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {interner_bill:.2f} lv")
print(f"Other: {other_bill:.2f} lv")
print(f"Average: {average:.2f} lv")

