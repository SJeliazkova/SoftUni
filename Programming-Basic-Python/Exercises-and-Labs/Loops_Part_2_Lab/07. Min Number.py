import sys
n = int(input())
counter = 0
min_num = sys.maxsize

while counter < n:
    num = int(input())
    if num < min_num:
        min_num = num

    counter += 1

print(min_num)