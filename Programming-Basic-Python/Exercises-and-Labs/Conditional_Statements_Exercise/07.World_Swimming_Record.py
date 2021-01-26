# от конзолата се въвежда рекрда, разстоянието и времето за 1 м
# забавяне на всеки 15 м с 12.5 секунди
# при изчисляването на забавянето се закръгля надолу
# изчисляване на времето на Иванчо и дали е подобри рекорда

import math
record = float(input())
distance = float(input())
time_per_meter = float(input())

swim_time = distance * time_per_meter
delay_time = math.floor(distance / 15) * 12.5
total_time = swim_time + delay_time

if total_time < record:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    need_seconds = total_time - record
    print(f"No, he failed! He was {need_seconds:.2f} seconds slower.")