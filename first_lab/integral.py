from first_lab.function import input_func


def left_rectangles_integral(part_x, part_y):
    square = 0
    for i in range(len(part_x) - 1):
        square += abs(part_y[i] * (part_x[i + 1] - part_x[i]))
    return square

def right_rectangles_integral(part_x, part_y):
    square = 0
    for i in range(len(part_x) - 1):
        square += abs(part_y[i+1] * (part_x[i + 1] - part_x[i]))
    return square

def average_rectangles_integral(part_x, t):
    square = 0
    for i in range(len(part_x) - 1):
        average_x = (part_x[i] + part_x[i + 1]) / 2
        average_y = (input_func([average_x], t))[0]
        square += abs(average_y * (part_x[i + 1] - part_x[i]))
    return square

def trapezoid_f_integral(part_x, part_y):
    square = 0
    for i in range(len(part_x) - 1):
        square += abs(((part_y[i + 1] + part_y[i]) / 2) * (part_x[i + 1] - part_x[i]))
    return square

def parabola_f_integral(part_x, part_y, t):
    square = 0
    for i in range(len(part_x) - 1):
        average_x = (part_x[i] + part_x[i + 1]) / 2
        average_y = (input_func([average_x], t))[0]
        square += abs(((part_y[i] + 4 * average_y + part_y[i + 1]) / 6) * (part_x[i + 1] - part_x[i]))
    return square