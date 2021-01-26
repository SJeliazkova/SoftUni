# вход от конзолата на променливите
# изчисляване печалбата от плодовете и от зеленчуците поотделно ( цена * количество )
# изчисляване на общата печалба по курса на еврото
# приниране на резултата до 2 знак

vegetables_price = float(input())
fruits_price = float(input())
vegetables_quantity = float(input())
fruits_quantity = float(input())

vegetables_sum = vegetables_price * vegetables_quantity
fruits_sum = fruits_price * fruits_quantity
total_sum_lv = vegetables_sum + fruits_sum
total_sum_euro = total_sum_lv / 1.94

print(f"{total_sum_euro:.2f}")