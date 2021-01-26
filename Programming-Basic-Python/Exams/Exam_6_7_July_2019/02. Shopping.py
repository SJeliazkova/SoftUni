budget = float(input())
num_of_videocard = int(input())
num_of_processors = int(input())
num_of_ram_memory = int(input())

videocard_price = 250 * num_of_videocard
processor_price = videocard_price * 0.35 * num_of_processors
ram_memory_price = videocard_price * 0.10 * num_of_ram_memory

total_price = videocard_price + processor_price + ram_memory_price

if num_of_videocard > num_of_processors:
    total_price = total_price * 0.85

if total_price <= budget:
    left_money = budget - total_price
    print(f"You have {left_money:.2f} leva left!")
else:
    needed_money = total_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
