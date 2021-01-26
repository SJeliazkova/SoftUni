number_of_students = int(input())

top_grade = 0
mid_5_4_grade = 0
mid_4_3_grade = 0
fail_grade = 0
all_grades = 0

for num in range(1, number_of_students+1):
    grade = float(input())

    if grade >= 5.00:
        top_grade += 1
        all_grades += grade
    elif grade >= 4 and grade <= 4.99:
        mid_5_4_grade += 1
        all_grades += grade
    elif grade >= 3 and grade <= 3.99:
        mid_4_3_grade += 1
        all_grades += grade
    elif grade < 3.00:
        fail_grade += 1
        all_grades += grade

average = all_grades / number_of_students
top_grade_percent = top_grade / number_of_students * 100
mid_5_4_grade_percent = mid_5_4_grade / number_of_students * 100
mid_4_3_grade_percent = mid_4_3_grade / number_of_students * 100
fail_grade_percent = fail_grade / number_of_students * 100

print(f"Top students: {top_grade_percent:.2f}%")
print(f"Between 4.00 and 4.99: {mid_5_4_grade_percent:.2f}%")
print(f"Between 3.00 and 3.99: {mid_4_3_grade_percent:.2f}%")
print(f"Fail: {fail_grade_percent:.2f}%")
print(f"Average: {average:.2f}")