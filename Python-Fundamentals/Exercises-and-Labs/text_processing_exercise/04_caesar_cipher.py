text = input()

encrypted_text = ""

for i in range(len(text)):
    current_sign_num = ord(text[i])
    new_sign = chr(current_sign_num + 3)
    encrypted_text += new_sign

print(encrypted_text)
