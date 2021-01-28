n = int(input())
word = input()

text_list = []
word_included = []

for el in range(1, n + 1):
    current_text = input()
    text_list.append(current_text)

    if word in current_text:
        word_included.append(current_text)

print(text_list)
print(word_included)




