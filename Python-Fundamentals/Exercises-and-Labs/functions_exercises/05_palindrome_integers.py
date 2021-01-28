def is_palindrome(element):
    if element == element[::-1]:
        return True
    return False


items = input()
numbers = items.split(", ")

for el in numbers:
    print(is_palindrome(el))
