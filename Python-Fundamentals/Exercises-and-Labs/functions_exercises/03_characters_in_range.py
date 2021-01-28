def ascii_table_symbol(symbol_1, symbol_2):
    result = ""
    for i in range(ord(symbol_1) + 1, ord(symbol_2)):
        result += chr(i) + " "
    return result


s_1 = input()
s_2 = input()
print(ascii_table_symbol(s_1, s_2))