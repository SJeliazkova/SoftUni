str_1, str_2 = input().split()

min_len = min(len(str_1), len(str_2))

total_sum = 0

for i in range(min_len):
    total_sum += ord(str_1[i]) * ord(str_2[i])

if len(str_1) > len(str_2):
    bigger_str = str_1
else:
    bigger_str = str_2

for i in range(min_len, len(bigger_str)):
    total_sum += ord(bigger_str[i])

print(total_sum)


