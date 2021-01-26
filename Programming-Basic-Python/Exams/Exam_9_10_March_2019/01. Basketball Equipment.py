basketball_tax = int(input())

basketball_shoes = basketball_tax * 0.60
basketball_clothes = basketball_shoes * 0.80
basketball_ball = basketball_clothes / 4
basketball_accessories = basketball_ball / 5

sum_costs = basketball_tax + basketball_ball + basketball_clothes + basketball_shoes + basketball_accessories

print(f"{sum_costs:.2f}")