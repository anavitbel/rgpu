# Написание программы для численного интегрирования площади под кривой. Беленко А.В.

import math
from integrate_test import integrate_test
import integrate as int


if __name__ == '__main__':
#    integrate_test()
    print(int.integrate(lambda x: x, 0, 1))
    print(int.integrate(math.log2, -4, -3))
    print(int.integrate(math.sin, -4, -3))
#    print(int.integrate(lambda x: x, 0, 1) - 0.5)

#    print(int.async_integrate(lambda x: x, 0, 1, 1000))
#    print(timeit.timeit("int.async_integrate(math.sin, 0, 1)", setup="import integrate as int; import math", number = 100))
