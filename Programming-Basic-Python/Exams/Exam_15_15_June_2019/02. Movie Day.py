shooting_time = int(input())
number_of_scenes = int(input())
time_per_scene = int(input())

preparation_time = shooting_time * 0.15
total_time = preparation_time + number_of_scenes * time_per_scene

if total_time <= shooting_time:
    left_time = shooting_time - total_time
    print(f"You managed to finish the movie on time! You have {round(left_time)} minutes left!")
else:
    needed_time = total_time - shooting_time
    print(f"Time is up! To complete the movie you need {round(needed_time)} minutes.")