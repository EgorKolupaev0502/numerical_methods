def parabola(list_x, list_y):
    coef = [0] * 3
    for i in range(3):
        coef_tmp = coef_Lagrange_parabola(list_x[i], list_x[(i + 1) % 3], list_x[(i + 2) % 3], list_y[i])
        for j in range(3):
            coef[j] += coef_tmp[j]
    return coef

def coef_Lagrange_parabola(x1, x2, x3, y):
    coef = [0] * 3
    denominator = (x1 - x2) * (x1 - x3)
    coef[0] = (1 / denominator) * y
    coef[1] = (- (x2 + x3) / denominator) * y
    coef[2] = ((x2 * x3) / denominator) * y
    # print(coef)
    return coef

