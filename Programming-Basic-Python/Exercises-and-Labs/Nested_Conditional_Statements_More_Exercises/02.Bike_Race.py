juniors = int(input())
seniors = int(input())
type_of_route = input()

collected_money = 0
riders = juniors + seniors

if type_of_route == "trail":
    collected_money = juniors * 5.5 + seniors * 7
elif type_of_route == "cross-country":
    collected_money = juniors * 8 + seniors * 9.50
elif type_of_route == "downhill":
    collected_money = juniors * 12.25 + seniors * 13.75
elif type_of_route == "road":
    collected_money = juniors * 20 + seniors * 21.50

if type_of_route == "cross-country" and riders >= 50:
    collected_money = (juniors * 8 + seniors * 9.50) * 0.75

costs = collected_money * 0.05
final_collected_money = collected_money - costs

print(f"{final_collected_money:.2f}")