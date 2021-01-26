import math

type_of_year = input()
number_of_holidays = int(input())
weekends_at_home = int(input())

play_holidays = 2 / 3 * number_of_holidays
weekend_in_year = 48
free_weekends = weekend_in_year - weekends_at_home
play_weekends = free_weekends * 3/4
play_at_home = weekends_at_home
total_play = play_at_home + play_holidays + play_weekends

if type_of_year == "leap":
    total_play = total_play * 1.15

print(f"{format(math.floor(total_play))}")




