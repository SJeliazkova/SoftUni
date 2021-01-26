word = input()

powerful_word = ""
powerful_word_points = 0

while word != "End of words":
    word_len = len(word)
    symbol_sum = 0
    first_letter = word[0]

    for i in range(0, word_len):
        letter = word[i]
        letter_value = ord(word[i])
        symbol_sum += letter_value

    if first_letter == "a" or first_letter == "e" or first_letter == "i" or \
        first_letter == "o" or first_letter == 'y' or first_letter == "u" or \
        first_letter == "A" or first_letter == "E" or first_letter == "I" or \
        first_letter == "O" or first_letter == "Y" or first_letter == "U":

        result = symbol_sum * word_len
    else:
        result = round(symbol_sum / word_len)

    if result > powerful_word_points:
        powerful_word_points = result
        powerful_word = word

    word = input()

else:
    print(f"The most powerful word is {powerful_word} - {powerful_word_points}")