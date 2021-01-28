data = input()

courses = {}

while not data == "end":
    course_name, student_name = data.split(" : ")

    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)

    data = input()

ordered_courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))

for course_name, student_names in ordered_courses.items():
    print(f"{course_name}: {len(student_names)}")

    for name in sorted(student_names):
        print(f"-- {name}")