name = input()
class_counter = 1
sum_grade = 0
disband_counter = 0

while class_counter <= 12:
    grade = float(input())

    if grade < 4:
        disband_counter += 1

        if disband_counter == 2:
            break

        continue

    sum_grade += grade

    class_counter += 1

if class_counter == 13:
    average = sum_grade / 12
    print(f"{name} graduated. Average grade: {average:.2f}")

else:
    print(f"{name} has been excluded at {class_counter} grade")