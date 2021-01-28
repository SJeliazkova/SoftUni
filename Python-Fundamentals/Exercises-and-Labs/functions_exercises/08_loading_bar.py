def fill_bar(bar_list, num_bars_check):
    for index in range(num_bars_check):
        bar_list[index] = "%"
    return bar_list


bar = []

for n in range(10):
    bar.append(".")

percent = int(input())
bars_to_fill = percent // 10

filled_bar = fill_bar(bar, bars_to_fill)

if percent < 100:
    print(f"{percent}% [{''.join(filled_bar)}]")
    print("Still loading...")
else:
    print("100% Complete!")
    print(f"[{''.join(filled_bar)}]")


