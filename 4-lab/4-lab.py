import numpy as np
import matplotlib.pyplot as plt


def simpson_integral(f, a, b, n=1000):
    x = np.linspace(a, b, n)
    y = f(x)

    square = 0
    for i in range(len(x) - 1):
        average_x = (x[i] + x[i + 1]) / 2
        average_y = f(average_x)
        square += abs(((y[i] + 4 * average_y + y[i + 1]) / 6) * (x[i + 1] - x[i]))
    return square

def gauss(A, b):
    n = len(b)
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            b[k] -= factor * b[i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= A[k][i] * x[i]

    return x

def solve_galerkin(N, p_func, q_func, f_func, h=1e-5, a=-1, b=1, num_points=1000):

    def phi(i, t):
        return np.cos((i + 1) * np.pi * (t + 1) / 2)

    def derivative(f, t, h):
        return (f(t + h) - f(t - h)) / (2 * h)

    def second_derivative(f, t, h):
        return (f(t - h) - 2 * f(t) + f(t + h)) / (h ** 2)

    def L_phi(i, t):
        def phi_t(t):
            return phi(i, t)

        phi_prime = derivative(phi_t, t, h)
        phi_double_prime = second_derivative(phi_t, t, h)

        return phi_double_prime + p_func(t) * phi_prime + q_func(t) * phi(i, t)

    A = [[0.0 for _ in range(N)] for _ in range(N)]
    b_vec = [0.0 for _ in range(N)]

    for i in range(N):
        for j in range(N):
            def integrand_A(t):
                return L_phi(j, t) * phi(i, t)

            A[i][j] = simpson_integral(integrand_A, a, b)

        def integrand_b(t):
            return f_func(t) * phi(i, t)

        b_vec[i] = simpson_integral(integrand_b, a, b)

    C = gauss(A, b_vec)

    def x_N(t):
        return sum(C[i] * phi(i, t) for i in range(N))

    return x_N, C

def main():
    N = 8
    a, b = -1, 1

    p_func = lambda t: -t
    q_func = lambda t: t ** 2
    f_func = lambda t: np.exp(-t ** 2)

    x_N, C = solve_galerkin(N, p_func, q_func, f_func)

    print("Коэффициенты разложения:")
    for i, c in enumerate(C):
        print(f"C[{i}] = {c:.6f}")

    t_values = np.linspace(a, b, 100)
    x_values = [x_N(t) for t in t_values]

    plt.figure(figsize=(10, 6))
    plt.plot(t_values, x_values, label=f'Приближенное решение (N={N})')
    plt.title('Решение краевой задачи методом Галеркина (вариант 8)')
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()