destination = input()
money_for_travel = 0

while destination != 'End':
    budget = float(input())
    while money_for_travel < budget:
        saved_money = float(input())
        money_for_travel += saved_money
    else:
        print(f'Going to {destination}!')
        money_for_travel = 0

    destination = input()