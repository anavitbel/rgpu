import math

x_ln = 0.5
x_arctan = math.pi / 6
array_ln = [0, 0.9974442, -0.471289, 0.2256685, -0.0587527]
array_arctan = [0.9999999953, -0.3333329248, 0.199989259, -0.1427243942, 0.1101791217, -0.0867899197, 0.0647029924,
               -0.0411720745, 0.0197433754, -0.0060738765, 0.0008766095]
n_ln = 1
n_arctan = 0


def menu():  # Меню
    print("Вычисление элементарных функций\n1. ln(1 + x)\n2. arctg x\n3. Выйти из программы")
    user_input = int(input())
    if user_input == 1:
        ln(x_ln, array_ln, n_ln)
    elif user_input == 2:
        arctan(x_arctan, array_arctan, n_arctan)
    elif user_input == 3:
        pass
    else:
        print("Введите число от 1 до 3.\n")
        menu()


def ln(x, array, n):
    summa = 0
    while n <= 4:
        f = array[n] * x ** n
        summa += f
        n += 1
    print("ln(1 + x) = {:.6f}".format(summa) + "\n")
    menu()


def arctan(x, array, n):
    summa = 0
    while n <= 10:
        f = array[n] * x ** (2 * n + 1)
        summa += f
        n += 1
    print("arctg x = {:.6f}".format(summa) + "\n")
    menu()


menu()
