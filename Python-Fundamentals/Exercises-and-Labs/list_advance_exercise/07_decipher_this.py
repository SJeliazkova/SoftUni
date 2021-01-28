text = input().split()
result = []


def is_digits(w):
    num = ""

    for i in w:
        if i.isdigit():
            num += i
    return num


for word in text:
    num_in_word = int(is_digits(word))
    letter = chr(num_in_word)

    word = list(word)

    word = [el for el in word if not (el.isdigit())]

    word.insert(0, letter)
    word[1], word[-1] = word[-1], word[1]

    result.append("".join(word))


print(" ".join(result))




