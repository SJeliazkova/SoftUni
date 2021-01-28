def repeat_str(string, n):
    result = ""
    for i in range(0, n):
        result += string
    return result

text = input()
rep = int(input())
print(repeat_str(text, rep))