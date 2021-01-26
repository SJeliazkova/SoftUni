inherited_money = float(input())
final_year = int(input())

needed_money = 0

for year in range(1800, final_year + 1):
    if year % 2 == 0:
        needed_money += 12000
    else:
        needed_money += 12000 + 50 * (year - 1800 + 18)

if needed_money <= inherited_money:
    left_money = inherited_money - needed_money
    print(f"Yes! He will live a carefree life and will have {left_money:.2f} dollars left.")

else:
    not_enought_money = needed_money - inherited_money
    print(f"He will need {not_enought_money:.2f} dollars to survive.")


