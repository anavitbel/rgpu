from integrate import integrate
import math
import pytest


def integrate_test():
    print(integrate(lambda x: x, 0, 1) - 0.5)
    assert math.fabs(integrate(lambda x: x, 0, 1) - 0.5) <= 0.00001
#    assert math.fabs(integrate(lambda x: math.sqrt(4 - x**2), -2,
#                     2) / 2 - math.pi) <= 10**-5

    with pytest.raises(ValueError):
        integrate(math.log2, -4, -3)

# почему-то погрешность здесь и в main отличается...