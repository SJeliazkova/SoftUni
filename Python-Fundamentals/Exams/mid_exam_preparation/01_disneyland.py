journey_cost = int(input())
months = int(input())

saved_money = 0

for month in range(1, months + 1):
    if month % 2 != 0 and month != 1:
        spent_money = saved_money * 0.16
        saved_money -= spent_money

    if month % 4 == 0:
        bonus = 0.25 * saved_money
        saved_money += bonus

    saved_money += journey_cost * 0.25

if saved_money > journey_cost:
    money_for_souvenirs = saved_money - journey_cost
    print(f"Bravo! You can go to Disneyland and you will have"
          f" {money_for_souvenirs:.2f}lv. for souvenirs.")

else:
    need_money = journey_cost - saved_money
    print(f"Sorry. You need {need_money:.2f}lv. more.")
