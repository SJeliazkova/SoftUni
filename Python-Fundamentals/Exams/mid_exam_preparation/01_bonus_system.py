students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

max_bonus = 0
max_bonus_student = 0

if students_count > 0:
    for student in range(students_count):
        attendances = int(input())

        if attendances == 0:
            total_bonus = 0
        else:
            total_bonus = attendances / lectures_count * (5 + additional_bonus)

            if total_bonus >= max_bonus:
                max_bonus = total_bonus
                max_bonus_student = attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_bonus_student} lectures.")