start_letter = input()
end_letter = input()
letter_skip = input()

counter = 0

for i in range(ord(start_letter), ord(end_letter)+1):
    for j in range(ord(start_letter), ord(end_letter)+1):
        for k in range(ord(start_letter), ord(end_letter)+1):

            if i == ord(letter_skip) or j == ord(letter_skip) or k == ord(letter_skip):
                continue
            else:
                counter += 1
                print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")

print(counter)


