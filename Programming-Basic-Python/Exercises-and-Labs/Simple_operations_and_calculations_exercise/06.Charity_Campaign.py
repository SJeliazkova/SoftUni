# вход от конзолата на всички променливи
# печалба от торти = брой торти * брой сладкари * брой дни * 45
# печалба от гофрети = брой гофрети * брой сладкари * брой дни * 5.80
# печалба палачинки = брой палачинки * брой сладкари * брой дни * 3.20
# обща сума = печалба торти + печалба гофрети + печалба палачинки
# разходи = обща сума / 8
# събрани дарения = обща сума - разходи
# принт събрани дарения до 2 знак

days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

profit_of_cakes = days * bakers * cakes * 45
profit_of_waffles = days * bakers * waffles * 5.80
profit_of_pancakes = days * bakers * pancakes * 3.20

sum = profit_of_cakes + profit_of_pancakes + profit_of_waffles
costs = sum / 8
total_donations = sum - costs

print(f"{total_donations:.2f}")