judge_count = int(input())

presentation_name = input()
sum_all_grades = 0
grades_counter = 0

while presentation_name != "Finish":
    sum_grade = 0
    for i in range(1, judge_count + 1):
        grade = float(input())
        sum_grade += grade
        sum_all_grades += grade
        grades_counter += 1

    average_grade = sum_grade / judge_count

    print(f"{presentation_name} - {average_grade:.2f}.")

    presentation_name = input()

average_all_grades = sum_all_grades / grades_counter

print(f"Student's final assessment is {average_all_grades:.2f}.")
