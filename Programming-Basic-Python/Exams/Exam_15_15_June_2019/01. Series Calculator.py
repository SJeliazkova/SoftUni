import math
series_name = input()
seasons_count = int(input())
episods_count = int(input())
duration = float(input())

advertising = duration * 0.20
episod_with_adv = duration + advertising
total_duration = seasons_count * episods_count * episod_with_adv + seasons_count * 10

print(f"Total time needed to watch the {series_name} series is {math.floor(total_duration)} minutes.")