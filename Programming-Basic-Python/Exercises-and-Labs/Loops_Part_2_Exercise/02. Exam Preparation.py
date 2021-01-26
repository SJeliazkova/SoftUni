number_of_poor_grades = int(input())

times_faild = 0
number_of_problems = 0
grades_sum = 0
last_problem = ""
has_failed = True


while times_faild < number_of_poor_grades:
    problem_name = input()

    if problem_name == "Enough":
        has_failed = False
        break

    grade = int(input())

    if grade <= 4:
        times_faild += 1
        grades_sum += grade
        number_of_problems += 1
        last_problem = problem_name
    else:
        grades_sum += grade
        number_of_problems += 1
        last_problem = problem_name

if has_failed:
    print(f"You need a break, {times_faild} poor grades.")
else:
    average = grades_sum / number_of_problems
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")


