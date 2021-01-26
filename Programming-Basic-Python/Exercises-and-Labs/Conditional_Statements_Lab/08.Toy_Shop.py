excursion_price = float(input())
puzzle_cnt = int(input())
talking_dolls_cnt = int(input())
taddy_bear_cnt = int(input())
mininons_cnt = int(input())
truks_cnt = int(input())

# Пъзел - 2.60 лв.
puzzle_price = 2.60
# Говореща кукла - 3 лв.
talking_dolls_price = 3
# Плюшено мече - 4.10 лв.
taddy_bear_price = 4.10
# Миньон - 8.20 лв.
mininons_price = 8.20
# Камионче - 2 лв.
truks_price = 2

toys_sum = puzzle_cnt + talking_dolls_cnt + taddy_bear_cnt + mininons_cnt + truks_cnt
total_sum = puzzle_cnt * puzzle_price + taddy_bear_cnt * taddy_bear_price + talking_dolls_cnt * talking_dolls_price + mininons_cnt * mininons_price + truks_cnt * truks_price

if toys_sum >= 50:
    total_sum = total_sum * 0.75

money_for_excursion = total_sum * 0.90

if money_for_excursion >= excursion_price:
    money_left = money_for_excursion - excursion_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_need = excursion_price - money_for_excursion
    print(f"Not enough money! {money_need:.2f} lv needed.")
