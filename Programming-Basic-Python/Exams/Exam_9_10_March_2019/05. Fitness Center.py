people_in_fitness = int(input())

back_people = 0
chest_people = 0
legs_people = 0
abs_people = 0
protein_shake = 0
protein_bar = 0
work_out = 0
protein = 0

for i in range(1, people_in_fitness + 1):
    action = input()
    if action == "Back":
        back_people += 1
        work_out += 1
    elif action == "Chest":
        chest_people += 1
        work_out += 1
    elif action == "Legs":
        legs_people += 1
        work_out += 1
    elif action == "Abs":
        abs_people += 1
        work_out += 1
    elif action == "Protein shake":
        protein_shake += 1
        protein += 1
    elif action == "Protein bar":
        protein_bar += 1
        protein += 1

work_out_percent = work_out / people_in_fitness * 100
protein_percent = protein / people_in_fitness * 100

print(f"{back_people} - back")
print(f"{chest_people} - chest")
print(f"{legs_people} - legs")
print(f"{abs_people} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{work_out_percent:.2f}% - work out")
print(f"{protein_percent:.2f}% - protein")
