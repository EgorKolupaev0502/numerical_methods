import numpy as np

def square(value_func, left_border, right_border):
    return value_func * (right_border - left_border)

def part_x(a, b, n):
    x = [float(i) for i in np.arange(a, b, (b - a) / n)]
    x.append(b)
    return x

def get_max_precision(list_number):
    return max([get_precision(list_number[i]) for i in range(len(list_number))])

def get_precision(number):
    str_f = str(number)
    if '.' not in str_f:
        return 0
    return len(str_f[str_f.index('.') + 1:])
