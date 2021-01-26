import sys
n = int(input())
counter = 0
max_num = - sys.maxsize

while counter < n:
    num = int(input())
    if num > max_num:
        max_num = num

    counter += 1

print(max_num)