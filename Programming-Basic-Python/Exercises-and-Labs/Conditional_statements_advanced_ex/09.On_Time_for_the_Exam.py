exam_hour = int(input())
exam_minutes = int(input())
student_hour = int(input())
student_minutes = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minutes
student_time_in_minutes = student_hour * 60 + student_minutes

if student_time_in_minutes > exam_time_in_minutes:
    print("Late")
elif student_time_in_minutes == exam_time_in_minutes or \
    exam_time_in_minutes <= (student_time_in_minutes + 30):
    print("On time")
elif exam_time_in_minutes > (student_time_in_minutes + 30):
    print("Early")

come_time = exam_time_in_minutes - student_time_in_minutes
if come_time > 0:
    if come_time // 60 > 0:
        come_time_hour = come_time // 60
        come_time_min = come_time % 60
        if (come_time_min % 60) < 10:
            print(f'{come_time_hour}:0{come_time_min} hours before the start')
        else:
            print(f'{come_time_hour}:{come_time_min} hours before the start')
    elif come_time % 60 > 0:
        print(f'{come_time} minutes before the start')
elif come_time < 0:
    come_time = abs(come_time)
    if come_time // 60 > 0:
        come_time_hour = come_time // 60
        come_time_min = come_time % 60
        if (come_time_min % 60) < 10:
            print(f'{come_time_hour}:0{come_time_min} hours after the start')
        else:
            print(f'{come_time_hour}:{come_time_min} hours after the start')
    elif come_time % 60 > 0:
        print(f'{come_time} minutes after the start')
