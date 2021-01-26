hours = int(input())
minutes = int(input())

sum_minutes = hours * 60 + minutes
total_minutes = sum_minutes + 15

final_hour = total_minutes // 60
final_minutes = total_minutes % 60

if final_hour == 24:
    final_hour = 0
if final_minutes <= 9:
    print(f"{final_hour}:0{final_minutes}")
else:
    print(f"{final_hour}:{final_minutes}")