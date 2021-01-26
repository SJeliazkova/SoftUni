easter_bread_count = int(input())

max_sum = 0
winner = ""

for i in range(1, easter_bread_count + 1):
    baker_name = input()
    command = input()
    grade_sum = 0

    while command != "Stop":
        grade = int(command)
        grade_sum += grade

        command = input()

    else:
        print(f"{baker_name} has {grade_sum} points.")

    if grade_sum > max_sum:
        max_sum = grade_sum
        winner = baker_name
        print(f"{winner} is the new number 1!")

print(f"{winner} won competition with {max_sum} points!")