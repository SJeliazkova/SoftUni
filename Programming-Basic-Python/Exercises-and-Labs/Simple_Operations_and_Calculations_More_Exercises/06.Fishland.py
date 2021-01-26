# въвеждане на прменливите от конзолата
# цена на паламуда = цена скумрия * 1.6
# цена сафрид = цена цаца * 1.8
# цена миди = 7.50
# изчисляване цена * килограми на паламуда, сафрида и мидите
# изчисляване на общата сума и принт на резултата до 2 знак

skumriq_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = float(input())

palamud_price = skumriq_price * 1.6
safrid_price = caca_price * 1.8
midi_price = 7.50
total_sum = palamud_kg * palamud_price + safrid_kg * safrid_price + midi_kg * midi_price
print(f"{total_sum:.2f}")