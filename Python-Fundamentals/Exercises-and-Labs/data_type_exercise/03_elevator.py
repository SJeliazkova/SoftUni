import math

number_of_person = int(input())
capacity = int(input())

courses = math.ceil(number_of_person / capacity)

print(courses)