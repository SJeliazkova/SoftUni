#въвеждане на променливи за дължина, ширина и височина
#въвеждане на променлива за процент зает обем
#изчисляване на обема в см
#изчисляване на обем литри
#изчисляване на необходимите литри (обема * 0.83)

length = int(input())
width = int(input())
height = int(input())
percent_of_volume = float(input())

volume_cm = length * width * height
volume_l = volume_cm * 0.001
free_volume_l = volume_l * ((100 - percent_of_volume)/100)

print(f"{free_volume_l:.3f}")