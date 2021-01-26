width = int(input())
lenght = int(input())
height = int(input())

free_volume = width * lenght * height

boxes_input = input()
boxes = 0

while boxes_input != "Done":
    boxes = int(boxes_input)

    if free_volume < boxes:
        break

    free_volume -= boxes

    boxes_input = input()

if boxes_input == "Done":
    print(f"{free_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {boxes - free_volume} Cubic meters more.")
