import math

hours = int(input())
days = int(input())
workers = int(input())

days_for_work = days * 0.9
hours_for_work = math.floor(days_for_work * 8 + workers * days * 2)

if hours_for_work >= hours:
    left_time = hours_for_work - hours
    print(f"Yes!{left_time} hours left.")
else:
    needed_time = hours - hours_for_work
    print(f"Not enough time!{needed_time} hours needed.")