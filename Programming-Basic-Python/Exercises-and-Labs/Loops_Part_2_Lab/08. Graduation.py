name = input()
class_counter = 1
sum_grade = 0

while class_counter <= 12:
    grade = float(input())

    if grade < 4:
        continue

    sum_grade += grade

    class_counter += 1

average = sum_grade / 12
print(f"{name} graduated. Average grade: {average:.2f}")