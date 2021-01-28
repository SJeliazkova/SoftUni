numbers = input()
opposite_numbers = []

list_nums = numbers.split()

for i in range(0, len(list_nums)):
    current_num = int(list_nums[i])
    opposite_num = current_num * (-1)
    opposite_numbers.append(opposite_num)

print(opposite_numbers)

