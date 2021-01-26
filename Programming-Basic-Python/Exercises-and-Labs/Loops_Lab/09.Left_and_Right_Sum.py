n = int(input())
sum_l = 0
sum_r = 0

for i in range(0, n):
    num = int(input())
    sum_l += num

for i in range(0, n):
    num = int(input())
    sum_r += num

if sum_l == sum_r:
    print(f"Yes, sum = {sum_r}")
else:
    diff = abs(sum_r - sum_l)
    print(f"No, diff = {diff}")
