import numpy as np
from matplotlib import pyplot as plt

import column_diagram_renderer as cdr
import input_x
import another

def input_func(x):
    # MAIN_FUNCTION
    return np.sin(x)

def input_func_render(a, b):
    x = np.arange(a, b, 0.01)
    y = input_func(x)
    plt.plot(x, y, color='red', linewidth=2)

def left_rectangles(part_x, part_y):
    input_func_render(part_x[0], part_x[len(part_x) - 1])
    list_x = []
    list_y = []
    square = 0
    for i in range(len(part_x) - 1):
        list_x.append([part_x[i], part_x[i+1]])
        list_y.append([part_y[i], part_y[i]])
        square += abs(part_y[i] * (part_x[i + 1] - part_x[i]))
    cdr.straight_columns_renderer(list_x, list_y)
    print(f"Формула левых прямоугольников: S = {square}")

def right_rectangles(part_x, part_y):
    input_func_render(part_x[0], part_x[len(part_x) - 1])
    list_x = []
    list_y = []
    square = 0
    for i in range(len(part_x) - 1):
        list_x.append([part_x[i], part_x[i+1]])
        list_y.append([part_y[i+1], part_y[i+1]])
        square += abs(part_y[i+1] * (part_x[i + 1] - part_x[i]))
    cdr.straight_columns_renderer(list_x, list_y)
    print(f"Формула правых прямоугольников: S = {square}")

def average_rectangles(part_x):
    input_func_render(part_x[0], part_x[len(part_x) - 1])
    list_x = []
    list_y = []
    square = 0
    for i in range(len(part_x) - 1):
        average_x = (part_x[i] + part_x[i + 1]) / 2
        average_y = input_func(average_x)
        list_x.append([part_x[i], part_x[i+1]])
        list_y.append([average_y, average_y])
        square += abs(average_y * (part_x[i + 1] - part_x[i]))
    cdr.straight_columns_renderer(list_x, list_y)
    print(f"Формула средних прямоугольников: S = {square}")

def trapezoid_f(part_x, part_y):
    input_func_render(part_x[0], part_x[len(part_x) - 1])
    list_x = []
    list_y = []
    square = 0
    for i in range(len(part_x) - 1):
        list_x.append([part_x[i], part_x[i + 1]])
        list_y.append([part_y[i], part_y[i + 1]])
        square += abs(((part_y[i + 1] + part_y[i]) / 2) * (part_x[i + 1] - part_x[i]))
    cdr.straight_columns_renderer(list_x, list_y)
    print(f"Формула трапеций: S = {square}")

def parabola_f(part_x, part_y):
    input_func_render(part_x[0], part_x[len(part_x) - 1])
    list_x = []
    list_y = []
    square = 0
    for i in range(len(part_x) - 1):
        average_x = (part_x[i] + part_x[i + 1]) / 2
        average_y = input_func(average_x)
        list_x.append([part_x[i], average_x, part_x[i + 1]])
        list_y.append([part_y[i], average_y, part_y[i + 1]])
        square += abs(((part_y[i] + 4 * average_y + part_y[i + 1]) / 6) * (part_x[i + 1] - part_x[i]))
    cdr.parabola_columns_renderer(list_x, list_y)
    print(f"Формула парабол: S = {square}")

def main():
    # a = input_x.input_parametr("a")
    # b = input_x.input_parametr("b")
    # e = input_x.input_parametr("e")
    a = 1
    b = 10
    e = 0.1
    part_x = another.part_x(a, b, e)
    part_y = input_func(part_x)
    left_rectangles(part_x, part_y)
    right_rectangles(part_x, part_y)
    average_rectangles(part_x)
    trapezoid_f(part_x, part_y)
    parabola_f(part_x, part_y)


if __name__ == "__main__":
    main()

