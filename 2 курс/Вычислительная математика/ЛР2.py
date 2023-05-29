import math

A = -10
B = 10
X0_newton = 2
E = 10 ** (-6)


def function(x):
    return x ** 2 - 3 + 0.5 ** x


def derivative_function(x):
    return 2 * x + 0.5 ** x * math.log(0.5)


def menu():  # Меню
    print("Решить нелинейное уравнение методом:\n1. Дихотомии\n2. Хорд\n"
          "3. Ньютона\n4. Выйти из программы")
    user_input = int(input())
    if user_input == 1:
        dichotomy()
    elif user_input == 2:
        chord()
    elif user_input == 3:
        newton()
    elif user_input == 4:
        pass
    else:
        print("Введите число от 1 до 4.\n")
        menu()


def dichotomy():  # Метод половинного деления (дихотомии)
    a = A
    b = B
    x = (a + b) / 2
    while abs(function(x)) >= E:
        x = (a + b) / 2
        a, b = (x, b) if function(x) * function(b) < 0 else (a, x)
    result = (a + b) / 2
    print("Результат при решении методом дихотомии: {:.5f}".format(result) + ".\n")
    menu()


def chord():  # Метод хорд
    previous_x = A
    current_x = B
    while abs(current_x - previous_x) >= E:
        x = current_x - ((current_x - previous_x) * function(current_x)) / \
            (function(current_x) - function(previous_x))
        previous_x = current_x
        current_x = x
    print("Результат при решении методом хорд: {:.5f}".format(current_x) + ".\n")
    menu()


def newton():  # Метод Ньютона
    previous_x = X0_newton
    current_x = previous_x - function(previous_x) / derivative_function(previous_x)
    while abs(current_x - previous_x) >= E:
        previous_x = current_x
        current_x = previous_x - function(previous_x) / derivative_function(previous_x)
    print("Результат при решении методом Ньютона: {:.5f}".format(current_x) + ".\n")
    menu()


menu()
