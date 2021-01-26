# въвеждане на трите времена от конзолата в секунди
# пресмятане на сумарнт време
# получаване на минутите чрез целочислено деление
# получаване на секундите чрез делене с остатък
# принтиране на резутата

time_1 = int(input())
time_2 = int(input())
time_3 = int(input())

sum_time = time_1 + time_2 + time_3
min = sum_time // 60
sec = sum_time % 60

if sec < 10:
    print(f"{min}:0{sec}")
else:
    print(f"{min}:{sec}")

