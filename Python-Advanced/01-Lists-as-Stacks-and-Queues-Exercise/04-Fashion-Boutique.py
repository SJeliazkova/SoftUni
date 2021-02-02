box = list(map(int, input().split()))
capacity = int(input())

counter_racks = 1
current_capacity = capacity

while box:
    current_clothes = box.pop()

    if current_capacity >= current_clothes:
        current_capacity -= current_clothes
    else:
        box.append(current_clothes)
        counter_racks += 1
        current_capacity = capacity

print(counter_racks)




