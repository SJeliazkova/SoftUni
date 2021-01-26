# вход от конзолата
# проверка дали е четен или нечетен РД
# за нечетен получава играчка, пресмятане сумата от играчките
# за четен получава пари, пресмятане сумата на парите
# брат и взима по 1 лв на всеки четен РД, изваждаме от общите
# проверка дали всички събрани пари са достатъчни за пералня

age_lily = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_toy_price = 0
current_price = 0
even_years_total_price = 0
total_sum = 0

for yaer in range(1, age_lily + 1):
    if yaer % 2 == 0:
        current_price = yaer * 5
        current_price -= 1
        even_years_total_price += current_price

    else:
        total_toy_price += toy_price


total_sum = total_toy_price + even_years_total_price

if total_sum >= washing_machine_price:
    left_money = total_sum - washing_machine_price
    print(f"Yes! {left_money:.2f}")
else:
    need_money = washing_machine_price - total_sum
    print(f"No! {need_money:.2f}")