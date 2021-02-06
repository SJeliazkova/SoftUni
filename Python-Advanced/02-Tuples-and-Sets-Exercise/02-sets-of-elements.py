nums = input().split()

n = int(nums[0])
m = int(nums[1])

first_set = set()
second_set = set()

for _ in range(n):
    first_set.add(input())

for _ in range(m):
    second_set.add(input())

unique_nums = first_set.intersection(second_set)

for el in unique_nums:
    print(el)
