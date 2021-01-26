volume = int(input())
first_pipe = int(input())
second_pipe = int(input())
hours = float(input())

filled_volume = first_pipe * hours + second_pipe * hours

if filled_volume > volume:
    liters_more = filled_volume - volume
    print(f"For {hours} hours the pool overflows with {liters_more:.2f} liters.")
else:
    filled_volume_in_percent = filled_volume / volume * 100
    percent_first_pipe = first_pipe * hours / filled_volume * 100
    percent_second_pipe = second_pipe * hours / filled_volume * 100
    print(f"The pool is {filled_volume_in_percent:.2f}% full. Pipe 1: {percent_first_pipe:.2f}%. Pipe 2: {percent_second_pipe:.2f}%.")