moves = int(input())

result = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_num = 0

for i in range(1, moves+1):
    num = int(input())

    if num >= 0 and num <= 9:
        from_0_to_9 += 1
        result += num * 0.20
    elif num >= 10 and num <= 19:
        from_10_to_19 += 1
        result += num * 0.30
    elif num >= 20 and num <= 29:
        from_20_to_29 += 1
        result += num * 0.40
    elif num >= 30 and num <= 39:
        from_30_to_39 += 1
        result += 50
    elif num >= 40 and num <= 50:
        from_40_to_50 += 1
        result += 100
    elif num < 0 or num > 50:
        result /= 2
        invalid_num += 1

from_0_to_9_per = from_0_to_9 / moves * 100
from_10_to_19_per = from_10_to_19 / moves * 100
from_20_to_29_per = from_20_to_29 / moves * 100
from_30_to_39_per = from_30_to_39 / moves * 100
from_40_to_50_per = from_40_to_50 / moves * 100
invalid_num_per = invalid_num / moves * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {from_0_to_9_per:.2f}%")
print(f"From 10 to 19: {from_10_to_19_per:.2f}%")
print(f"From 20 to 29: {from_20_to_29_per:.2f}%")
print(f"From 30 to 39: {from_30_to_39_per:.2f}%")
print(f"From 40 to 50: {from_40_to_50_per:.2f}%")
print(f"Invalid numbers: {invalid_num_per:.2f}%")