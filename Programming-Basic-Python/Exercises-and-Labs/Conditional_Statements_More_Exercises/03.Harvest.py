import math
square_meters_vineyard = int(input())
grapes_per_square_meters = float(input())
wanted_wine_l = int(input())
workers = int(input())

total_grapes = square_meters_vineyard * grapes_per_square_meters
grapes_for_wine = total_grapes * 0.4
wine_l = grapes_for_wine / 2.5

if wine_l < wanted_wine_l:
    need_wine = wanted_wine_l - wine_l
    print(f'It will be a tough winter! More {format(math.floor(need_wine))} liters wine needed.')
else:
    extra_wine = wine_l - wanted_wine_l
    wine_per_worker = extra_wine / workers
    print(f'Good harvest this year! Total wine: {format(math.floor(wine_l))} liters.')
    print(f'{format(math.ceil(extra_wine))} liters left -> {format(math.ceil(wine_per_worker))} liters per person.')