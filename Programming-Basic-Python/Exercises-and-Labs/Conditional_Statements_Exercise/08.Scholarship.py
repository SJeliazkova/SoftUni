import math

income_lv = float(input())
average_success = float(input())
minimum_wage = float(input())

social_scholarship = math.floor(minimum_wage * 0.35)
grade_scholarship = math.floor(average_success * 25)

if average_success < 4.5:
    print("You cannot get a scholarship!")

elif 4.5 <= average_success < 5.5:
    if income_lv < minimum_wage:
              print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print("You cannot get a scholarship!")

elif average_success >= 5.50:
    if income_lv < minimum_wage:
        if social_scholarship > grade_scholarship:
            print(f"You get a Social scholarship {social_scholarship} BGN")
        else:
            print(f"You get a scholarship for excellent results {grade_scholarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {grade_scholarship} BGN")



