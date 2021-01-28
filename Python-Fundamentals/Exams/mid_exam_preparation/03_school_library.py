books = input().split("&")

command = input()

while not command == "Done":
    command = command.split(" | ")
    type_command = command[0]
    book_name = command[ 1 ]

    if type_command == "Add Book":
        if book_name not in books:
            books.insert(0, book_name)

    elif type_command == "Take Book":
        if book_name in books:
            books.remove(book_name)

    elif type_command == "Swap Books":
        book_1 = command[1]
        book_2 = command[2]
        if book_1 in books and book_2 in books:
            index_1 = books.index(book_1)
            index_2 = books.index(book_2)
            books[index_1], books[index_2] = books[index_2], books[index_1]

    elif type_command == "Insert Book":
        books.append(book_name)

    elif type_command == "Check Book":
        index = int(book_name)
        if index in range(len(books)):
            print(f"{books[index]}")

    command = input()

print(", ".join(books))

