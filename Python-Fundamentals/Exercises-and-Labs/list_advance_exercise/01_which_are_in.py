first_list = input().split(", ")
second_list = input().split(", ")

result = [substr for substr in first_list for word in second_list if substr in word]

print(sorted(set(result), key=result.index))


