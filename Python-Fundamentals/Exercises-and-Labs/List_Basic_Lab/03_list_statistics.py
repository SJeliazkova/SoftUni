n = int(input())

positive_list = []
negative_list = []

for num in range(1, n+1):
    current_num = int(input())

    if current_num < 0:
        negative_list.append(current_num)
    else:
        positive_list.append(current_num)

sum_of_negative = sum(negative_list)
positive_count = len(positive_list)

print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_count}. Sum of negatives: {sum_of_negative}")