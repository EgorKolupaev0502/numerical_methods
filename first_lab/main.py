import numpy as np
from matplotlib import pyplot as plt


import another
from first_lab.another import part_x
from first_lab.function import input_func
from first_lab.integral import left_rectangles_integral, right_rectangles_integral, average_rectangles_integral, \
    trapezoid_f_integral, parabola_f_integral




def input_func_render(a, b):
    x = np.arange(a, b, 0.01)
    y = input_func(x, 10)
    plt.plot(x, y, color='red', linewidth=2)

def left_rectangles(a, b, e, n, t):
    while 1:
        x1 = part_x(a, b, n)
        y1 = input_func(x1, t)
        i1 = left_rectangles_integral(x1, y1)
        x2 = part_x(a, b, 2 * n)
        y2 = input_func(x2, t)
        i2 = left_rectangles_integral(x2, y2)
        n = 2 * n
        if abs(i2 - i1) < e:
            break
    return i2

def right_rectangles(a, b, e, n, t):
    while 1:
        x1 = part_x(a, b, n)
        y1 = input_func(x1, t)
        i1 = right_rectangles_integral(x1, y1)
        x2 = part_x(a, b, 2 * n)
        y2 = input_func(x2, t)
        i2 = right_rectangles_integral(x2, y2)
        n = 2 * n
        if abs(i2 - i1) < e:
            break
    return i2

def average_rectangles(a, b, e, n, t):
    while 1:
        x1 = part_x(a, b, n)
        i1 = average_rectangles_integral(x1, t)
        x2 = part_x(a, b, 2 * n)
        i2 = average_rectangles_integral(x2, t)
        n = 2 * n
        if abs(i2 - i1) / 3 < e:
            break
    return i2

def trapezoid_f(a, b, e, n, t):
    while 1:
        x1 = part_x(a, b, n)
        y1 = input_func(x1, t)
        i1 = trapezoid_f_integral(x1, y1)
        x2 = part_x(a, b, 2 * n)
        y2 = input_func(x2, t)
        i2 = trapezoid_f_integral(x2, y2)
        n = 2 * n
        if abs(i2 - i1) / 3 < e:
            break
    return i2

def parabola_f(a, b, e, n, t):
    while 1:
        x1 = part_x(a, b, n)
        y1 = input_func(x1, t)
        i1 = parabola_f_integral(x1, y1, t)
        x2 = part_x(a, b, 2 * n)
        y2 = input_func(x2, t)
        i2 = parabola_f_integral(x2, y2, t)
        n = 2 * n
        if abs(i2 - i1) / 15 < e:
            break
    return i2

def main():
    # a = input_x.input_parametr("a")
    # b = input_x.input_parametr("b")
    # e = input_x.input_parametr("e")
    a = -10
    b = 10
    e = 0.01
    a_t =  - 10
    b_t = 10
    step_t = 0.1
    print("Methods:\n1 - left squares\n2 - right squares\n3 - average squares\n4 - trapezoid formula\n5 - parabola formula")

    while True:
        match int(input(" >>> ")):
            case 1:
                i_t = [left_rectangles(a, b, e, 1, t) for t in np.arange(a_t, b_t, step_t)]
                break
            case 2:
                i_t = [right_rectangles(a, b, e, 1, t) for t in np.arange(a_t, b_t, step_t)]
                break
            case 3:
                i_t = [average_rectangles(a, b, e, 1, t) for t in np.arange(a_t, b_t, step_t)]
                break
            case 4:
                i_t = [trapezoid_f(a, b, e, 1, t) for t in np.arange(a_t, b_t, step_t)]
                break
            case 5:
                i_t = [parabola_f(a, b, e, 1, t) for t in np.arange(a_t, b_t, step_t)]
                break
            case _:
                print("try again")
    t = np.arange(a, b, step_t)
    plt.figure(figsize=(10, 5))
    plt.plot(t, i_t)
    plt.show()


if __name__ == "__main__":
    main()