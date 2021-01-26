budget = float(input())

length_name = 0

command = input()
while command != "ACTION":
    length_name = len(command)
    if length_name <= 15:
        actor_salary = float(input())
        budget -= actor_salary
    else:
        actor_salary = 0.20 * budget
        budget -= actor_salary

    if budget <= 0:
        break
    else:
        command = input()

if budget >= 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    needed_money = abs(budget)
    print(f"We need {needed_money:.2f} leva for our actors.")

