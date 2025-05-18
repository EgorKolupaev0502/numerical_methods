import numpy as np


def input_func(x, t):
    # MAIN_FUNCTION
    return [ x_1 ** 2 * t ** 2 for x_1 in x]