control_min = int(input())
control_sec = int(input())
lenght = float(input())
sec_for_100 = int(input())

control_time = control_sec + control_min * 60
martin_time = lenght * sec_for_100 / 100 - (lenght / 120) * 2.5

if martin_time <= control_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {martin_time:.3f}.")
else:
    needed_sec = martin_time - control_time
    print(f"No, Marin failed! He was {needed_sec:.3f} second slower.")