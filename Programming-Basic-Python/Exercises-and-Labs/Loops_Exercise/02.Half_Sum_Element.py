import sys
n = int(input())
max = -sys.maxsize
sum_all = 0

for i in range(1, n + 1):
    value = int(input())
    sum_all += value

    if value > max:
        max = value

sum_other = sum_all - max
if max == sum_other:
    print("Yes")
    print(f"Sum = {sum_other}")
else:
    print("No")
    print(f"Diff = {abs(sum_other-max)}")