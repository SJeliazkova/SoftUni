command = input()

todo_list = [0 for _ in range(11)]

while command != "End":
    note = command.split("-")
    index = int(note[0])
    task = note[1]
    todo_list.pop(index)
    todo_list.insert(index, task)

    command = input()

result = [task for task in todo_list if not task == 0]

print(result)