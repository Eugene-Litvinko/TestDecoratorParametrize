import math

def sum_numbers(x):
    if x < 10:
        return x
    else:
        x1 = str(x)
        x2 = list(x1)
        x3 = map(int, x2)
        return sum(x3)

sum_numbers(99)



