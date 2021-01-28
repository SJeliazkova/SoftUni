words = input().split()
searched_palindrome = input()

palindromes = [word for word in words if word == word[::-1]]


print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")