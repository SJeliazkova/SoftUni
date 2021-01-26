import math
series_name = input()
episode_duration = int(input())
lunch_break = int(input())

time_for_lunch = lunch_break / 8
time_for_rest = lunch_break / 4

left_time_for_film = lunch_break - time_for_lunch - time_for_rest

if left_time_for_film >= episode_duration:
    left_time = left_time_for_film - episode_duration
    print(f"You have enough time to watch {series_name} and left with {math.ceil(left_time)} minutes free time.")

else:
    needed_time = episode_duration - left_time_for_film
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(needed_time)} more minutes.")