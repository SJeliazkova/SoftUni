n = int(input())

students = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

average_student = {}

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        average_student[name] = average_grade

average_student = sorted(average_student.items(), key=lambda x: (-x[1], x[0]))

for name, av_grade in average_student:
    print(f'{name} -> {av_grade:.2f}')


