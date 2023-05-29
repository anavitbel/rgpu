def fib_iter(iter):
    m = max(iter, key=lambda i: int(i))
    lst = fib1(m)
    res = []
    for i in range(len(lst)):
        if lst[i] in iter:
            res.append(lst[i])

    return res


def fib1(n):
    f = FibonacchiLst()
    while n >= f.result[-1]:
        f.result.append(f.result[-1] + f.result[-2])
    if n < f.result[-1]:
        f.result.pop()
    return f.result


def fib2(n):
    f = FibonacchiLst()
    for i in range(n - 2):
        f.result.append(f.result[-1] + f.result[-2])
    while n < len(f.result):
        f.result.pop()
    return f.result


class FibonacchiLst:
    def __init__(self):
        self.result = [0, 1]

    def __iter__(self):
        self.initial = self.result
        return self

    def __next__(self):
        self.initial.append(self.initial[-1] + self.initial[-2])


def test_fib_11():
    assert fib1(1) == [0, 1, 1], "Тривиальный случай n = 1, список [0, 1]"


def test_fib_12():
    assert fib1(4) == [0, 1, 1, 2, 3], "fib(4) должно быть [0, 1, 1, 2, 3]"


def test_fib_21():
    assert fib2(1) == [0], "fib(1) должно быть [0]"


def test_fib_22():
    assert fib2(5) == [0, 1, 1, 2, 3], "fib(1) должно быть [0, 1, 1, 2, 3]"


if __name__ == '__main__':
    test_fib_11()
    test_fib_12()
    test_fib_21()
    test_fib_22()
    fib_iter([1, 2, 6, 4, 8, 21, 100, 0])
    print(
        "1. Вывести числа ряда Фибоначчи, не превышающие число n.\n2. Вывести первые n чисел ряда Фибоначчи.\n3. Пример работы функции fib_iter.\nЧто выберите?"
    )
    ans = str(input())

    if ans == "1":
        n = int(input("Введите целое число n:"))
        print(fib1(n))
    elif ans == "2":
        n = int(input("Введите целое число n:"))
        print(fib2(n))
    elif ans == "3":
        print(fib_iter(list(range(14))))
    else:
        print("Я не смог распознать ваш ответ... Попробуйте ещё раз.")