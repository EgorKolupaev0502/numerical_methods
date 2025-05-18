import numpy as np
import matplotlib.pyplot as plt


def bisection_method(f, a, b, epsilon):
    if np.sign(f(a)) == np.sign(f(b)):
        return None  # Нет решения или несколько решений
    while 1:
        c = (a + b) / 2
        if abs(f(c)) < epsilon:
            return c
        if np.sign(f(a)) != np.sign(f(c)):
            b = c
        else:
            a = c



def newton_method(f, df, x0, epsilon, max_iter=1000):
    x_prev = x0
    for _ in range(max_iter):
        fx = f(x_prev)
        dfx = df(x_prev)
        if dfx == 0:  # Защита от деления на ноль
            return None
        x_next = x_prev - fx / dfx
        if abs(x_next - x_prev) < epsilon:
            return x_next
        x_prev = x_next


def find_roots(f, df, a, b, method, epsilon, step=0.1, newton_initial_guesses=10):
    roots = set()
    # Разбиваем отрезок на подотрезки для поиска корней
    segments = []
    x = a
    while x < b:
        segments.append((x, min(x + step, b)))
        x += step

    for segment in segments:
        seg_a, seg_b = segment
        if method == 'bisection':
            # Проверяем изменение знака на подотрезке
            if np.sign(f(seg_a)) != np.sign(f(seg_b)):
                root = bisection_method(f, seg_a, seg_b, epsilon)
                if root is not None:
                    roots.add(round(root / epsilon) * epsilon)  # Округление для избежания дубликатов
        elif method == 'newton':
            # Пробуем несколько начальных точек в подотрезке
            for guess in np.linspace(seg_a, seg_b, newton_initial_guesses):
                root = newton_method(f, df, guess, epsilon)
                if root is not None and a <= root <= b:
                    roots.add(round(root / epsilon) * epsilon)

    return sorted(roots)


def plot_solutions(mu_values, roots_dict, method_name):
    plt.figure(figsize=(10, 6))
    for mu in mu_values:
        if mu in roots_dict:
            for root in roots_dict[mu]:
                plt.plot(mu, root, 'bo')
    plt.xlabel('μ')
    plt.ylabel('x')
    plt.title(f'Решения уравнения f(x, μ) = 0 ({method_name} метод)')
    plt.grid(True)
    plt.show()


def main():
    # Ввод параметров
    # a = float(input("Введите a (начало отрезка по x): "))
    # b = float(input("Введите b (конец отрезка по x): "))
    # alpha = float(input("Введите α (начало отрезка по μ): "))
    # beta = float(input("Введите β (конец отрезка по μ): "))
    # epsilon = float(input("Введите точность ε: "))
    a = -2
    b = 2
    alpha = -4
    beta = 1
    epsilon = 0.01
    mu_step = 0.01

    # Выбор метода
    method = input("Выберите метод (bisection/newton): ").strip().lower()
    while method not in ['bisection', 'newton']:
        print("Некорректный метод. Выберите 'bisection' или 'newton'")
        method = input("Выберите метод (bisection/newton): ").strip().lower()

    # def f(x, mu):
    #     return x ** 2 - x * ( 2 * mu + 2) + mu ** 2 + 2 * mu
    #
    # def df(x, mu):
    #     return 2 * x - (2 * mu + 2)

    def f(x, mu):
        return x**2 + mu

    def df(x, mu):
        return 2 * x

    # Нахождение решений для каждого μ
    mu_values = np.arange(alpha, beta + mu_step, mu_step)
    roots_dict = {}

    for mu in mu_values:
        # Создаем частично примененные функции для текущего mu
        def f_mu(x):
            return f(x, mu)

        def df_mu(x):
            return df(x, mu)

        if method == 'bisection':
            roots = find_roots(f_mu, df_mu, a, b, 'bisection', epsilon)
        else:
            roots = find_roots(f_mu, df_mu, a, b, 'newton', epsilon)

        if roots:
            roots_dict[mu] = roots

    # Вывод результатов
    print("\nРешения уравнения:")
    for mu in sorted(roots_dict.keys()):
        for root in roots_dict[mu]:
            print(f"μ = {mu:.3f}, x = {root:.5f}")

    # Визуализация
    plot_solutions(mu_values, roots_dict, method)


if __name__ == "__main__":
    main()