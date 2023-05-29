import math

number_of_splits = [10, 50, 150]


def menu():  # Меню
    print("\nЧисленные методы решения дифференциальных уравнений\n1. Метод Эйлера\n2. Метод Рунге-Кутта\n"
          "3. ДУ 2-го порядка\n4. Система ДУ\n5. Выйти из программы")
    user_input = int(input())
    if user_input == 1:
        euler_method()
    elif user_input == 2:
        runge_kutta_method()
    elif user_input == 3:
        second_order_de()
    elif user_input == 4:
        system_of_de()
    elif user_input == 5:
        pass
    else:
        print("Введите число от 1 до 5.")
        menu()


def euler_method():  # Решение дифференциального уравнения методом Эйлера
    def f(x, y):
        return y * (1 - x)

    a = 0
    b = 1
    for n in number_of_splits:
        h = (b - a) / n
        xi = a  # Интервал [0; 1]
        yi = 1  # Начальное условие y(0) = 1
        print(f"\nШаг интегрирования: {h}.")
        print(f"x0 = {xi:.6f}, y0 = {yi:.6f}.")
        for _ in range(n):
            yi += h * f(xi, yi)
            xi += h
            print(f"x = {xi:.6f}, y = {yi:.6f}.")
    menu()


def runge_kutta_method():  # Решение дифференциального уравнения методом Рунге-Кутта
    def f(x, y):
        return y * (1 - x)

    a = 0
    b = 1
    for n in number_of_splits:
        h = (b - a) / n
        xi = a
        yi = 1
        print(f"\nШаг интегрирования: {h}.")
        print(f"x0 = {xi:.6f}, y0 = {yi:.6f}.")
        for _ in range(n):
            k1 = h * f(xi, yi)
            k2 = h * f(xi + h / 2, yi + k1 / 2)
            k3 = h * f(xi + h / 2, yi + k2 / 2)
            k4 = h * f(xi + h, yi + k3)
            yi += ((k1 + 2 * k2 + 2 * k3 + k4) / 6)
            xi += h
            print(f"x = {xi:.6f}, y = {yi:.6f}.")
    menu()


def second_order_de():  # Решение дифференциального уравнения второго порядка
    h = 0.1

    def y1(y, z):
        return y + h * z

    def z1(x, y, z):
        return z + h * (-(z / x + y))

    xi = 1
    yi = 0.77
    zi = -0.44  # y'
    print(f"x0 = {xi:.6f}, y0 = {yi:.6f}, z0 = {zi:.6f}.")
    while xi <= 1.5:
        zi = z1(xi, yi, zi)
        yi = y1(yi, zi)
        xi += h
        print(f"x = {xi:.6f}, y = {yi:.6f}, z = {zi:.6f}.")
    menu()


def system_of_de():  # Решение системы дифференциальных уравнений
    def dx_dy(x, z):
        return -2 * x + 5 * z

    def dy_dt(t, x, y, z):
        return math.sin(t - 1) * x - y - 3 * z

    def dz_dt(x, z):
        return -x + 2 * z

    h = 0.001
    b = 0.3
    ti = 0
    xi = 2
    yi = 1
    zi = 1
    print(f"t0 = {ti:.6f}, x0 = {xi:.6f}, y0 = {yi:.6f}, z0 = {zi:.6f}.")
    while ti < b:
        yi += h * dy_dt(ti, xi, yi, zi)
        temporary = xi  # Текущий x
        xi += h * dx_dy(xi, zi)
        zi += h * dz_dt(temporary, yi)  # Текущий x
        print(f"t = {ti:.6f}, x = {xi:.6f}, y = {yi:.6f}, z = {zi:.6f}.")
        ti += h
    menu()


menu()
