import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator


def golden_section_search(f, a, b, tol=1e-5):
    phi = (1 + np.sqrt(5)) / 2  # Золотое сечение
    iterations = 0

    while abs(b - a) > tol:
        alpha = b - (b - a) / phi
        beta = a + (b - a) / phi

        if f(alpha) <= f(beta):
            b = beta
        else:
            a = alpha

        iterations += 1

    return (a + b) / 2


def coordinate_descent(f, x0, y0, epsilon=1e-5, max_iter=1000):
    x, y = x0, y0
    path = [(x, y)]

    for _ in range(max_iter):
        x_prev, y_prev = x, y

        def phi_x(xi):
            return f(xi, y)

        x = golden_section_search(phi_x, a, b, epsilon)

        def phi_y(yi):
            return f(x, yi)

        y = golden_section_search(phi_y, c, d, epsilon)

        path.append((x, y))

        if np.sqrt((x - x_prev) ** 2 + (y - y_prev) ** 2) < epsilon:
            break

    return x, y, path


def gradient_descent(f, grad_f, x0, y0, epsilon=1e-5, max_iter=1000):
    x, y = x0, y0
    path = [(x, y)]

    for _ in range(max_iter):
        grad = grad_f(x, y)
        grad_norm = np.sqrt(grad[0] ** 2 + grad[1] ** 2)

        if grad_norm < epsilon:
            break

        def phi(alpha):
            return f(x - alpha * grad[0], y - alpha * grad[1])

        alpha = golden_section_search(phi, 0, 1.0, epsilon)

        x_new = x - alpha * grad[0]
        y_new = y - alpha * grad[1]

        path.append((x_new, y_new))

        if np.sqrt((x_new - x) ** 2 + (y_new - y) ** 2) < epsilon:
            break

        x, y = x_new, y_new

    return x, y, path


def plot_contour_and_path(f, a, b, c, d, path, title):
    x_vals = np.linspace(a, b, 400)
    y_vals = np.linspace(c, d, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = f(X, Y)

    plt.figure(figsize=(10, 8))
    plt.contour(X, Y, Z, levels=20, cmap='viridis')
    plt.colorbar(label='f(x, y)')

    path_x, path_y = zip(*path)
    plt.plot(path_x, path_y, 'r.-', label='Путь оптимизации')
    plt.scatter(path_x[0], path_y[0], c='green', label='Начальная точка')
    plt.scatter(path_x[-1], path_y[-1], c='blue', label='Точка минимума')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()


# Пример функции и её градиента
# def f(x, y):
#     return (x**2 + y - 11)**2 + (x + y**2 - 7)**2
#
#
# def grad_f(x, y):
#     df_dx = 4*x*(x**2 + y - 11) + 2*(x + y**2 - 7)
#     df_dy = 2*(x**2 + y - 11) + 4*y*(x + y**2 - 7)
#     return np.array([df_dx, df_dy])

def f(x, y):
    return 2*x**2 + 5*y**2 + x*y

def grad_f(x, y):
    df_dx = 4*x + y
    df_dy = 10*y + x
    return np.array([df_dx, df_dy])


# Границы области
a, b = -5, 5
c, d = -5, 5

# Ввод пользователя
epsilon = float(input("Введите точность ε: "))
x0 = float(input("Введите начальную точку x0: "))
y0 = float(input("Введите начальную точку y0: "))
method = input("Выберите метод (1 - покоординатный спуск, 2 - градиентный спуск): ")

if method == '1':
    x_min, y_min, path = coordinate_descent(f, x0, y0, epsilon)
    title = 'Метод покоординатного спуска'
elif method == '2':
    x_min, y_min, path = gradient_descent(f, grad_f, x0, y0, epsilon)
    title = 'Метод наискорейшего градиентного спуска'
else:
    print("Неверный выбор метода.")
    exit()

print(f"Найденная точка минимума: ({x_min:.5f}, {y_min:.5f})")
print(f"Значение функции в точке минимума: {f(x_min, y_min):.5f}")

plot_contour_and_path(f, a, b, c, d, path, title)