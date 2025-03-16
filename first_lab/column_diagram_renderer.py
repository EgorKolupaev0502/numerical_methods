import numpy as np
from matplotlib import pyplot as plt

import first_lab.lagrange_formula as lg

def straight_columns_renderer(list_x, list_y):
    for i in range(len(list_x)):
        draw_straight_column(list_x[i][0], list_x[i][1], list_y[i][0], list_y[i][1])
    plt.show()

def draw_straight_column(x1, x2, y1, y2):
    x = [x1, x2]
    y = [y1, y2]
    draw_vertical_line(x, y)
    plt.fill_between(x, y, color='yellow')
    plt.plot(x, y, color='orange')

def parabola_columns_renderer(list_x, list_y):
    for i in range(len(list_x)):
        draw_parabola_column(list_x[i], list_y[i])
    plt.show()

def draw_parabola_column(list_x, list_y):
    coef_polynom = lg.parabola(list_x, list_y)
    # print(coef_polynom)
    x = np.linspace(list_x[0], list_x[2], 1000)
    y = coef_polynom[0] * (x ** 2) + coef_polynom[1] * x + coef_polynom[2]
    draw_vertical_line([list_x[0], list_x[2]], [list_y[0], list_y[2]])
    plt.fill_between(x, y, color='yellow')
    plt.plot(x, y, color='orange')

def draw_vertical_line(x, y):
    plt.plot([x[0], x[0]], [y[0], 0], color='orange')
    plt.plot([x[1], x[1]], [y[1], 0], color='orange')


