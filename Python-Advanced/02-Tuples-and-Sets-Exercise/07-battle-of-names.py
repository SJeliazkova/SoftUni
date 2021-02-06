n = int(input())

even_nums = set()
odd_nums = set()

for current_iter_count in range(1, n + 1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // current_iter_count

    if current_sum % 2 == 0:
        even_nums.add(current_sum)
    else:
        odd_nums.add(current_sum)

sum_evens = sum(even_nums)
sum_odds = sum(odd_nums)

if sum_evens == sum_odds:
    modified_set = [str(el) for el in even_nums.union(odd_nums)]
    print(f"{', '.join(modified_set)}")
elif sum_odds > sum_evens:
    modified_set = [ str(el) for el in odd_nums.difference(even_nums) ]
    print(f"{', '.join(modified_set)}")
else:
    modified_set = [ str(el) for el in even_nums.symmetric_difference(odd_nums) ]
    print(f"{', '.join(modified_set)}")
