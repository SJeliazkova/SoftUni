hall_rent = int(input())

figurine_price = hall_rent * 0.70
catering_price = figurine_price * 0.85
sound_system_price = catering_price / 2

total_costs = hall_rent + figurine_price + catering_price + sound_system_price

print(f"{total_costs:.2f}")