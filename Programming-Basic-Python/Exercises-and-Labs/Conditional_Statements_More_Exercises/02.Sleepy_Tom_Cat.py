days_off = int(input())

working_days = 365 - days_off
play_time = working_days * 63 + days_off * 127
play_time_norm = 30000

if play_time > play_time_norm:
    more_time = play_time - play_time_norm
    hours = more_time // 60
    minutes = more_time % 60
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    less_time = play_time_norm - play_time
    hours = less_time // 60
    minutes = less_time % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")