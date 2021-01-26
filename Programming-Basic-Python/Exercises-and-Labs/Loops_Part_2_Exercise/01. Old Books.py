searched_book = input()
books_in_library = int(input())

count_checked_book = 0

while books_in_library > 0:
    title = input()

    if title == searched_book:
        print(f"You checked {count_checked_book} books and found it.")
        break
    else:
        count_checked_book += 1

    books_in_library -= 1


if books_in_library <= 0:
    print("The book you search is not here!")
    print(f"You checked {count_checked_book} books.")



