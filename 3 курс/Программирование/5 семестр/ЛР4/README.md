# Лабораторная работа 4. Ряд Фибоначчи с помощью итераторов

При выполнении лабораторной работы были написаны:
* функция `fib1(n)` для вывода чисел ряда Фибоначчи, не превосходящих `n`
* функция `fib2(n)` для вывода `n` первых чисел ряда Фибоначчи
* четыре теста на проверку этих функций
* класс `FibonacciLst` с реализацией методов `__init__`,`__iter__`, `__next__`.
* функция `fib_iter(iter)`, выводящая числа ряда Фибоначчи в том случае, если эти числа есть в итерируемом объекте iter.