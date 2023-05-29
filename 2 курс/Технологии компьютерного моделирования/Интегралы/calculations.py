import math


def f14(x):
    return math.cos(x**2 + 0.6) / (0.7 + math.sin(0.8 * x + 1)
                                   )  #блин исправь формулу


def f14_2(x):
    return (x - 2) * math.cos(x) - 1


def f14_2_dev(x):
    return (2 - x) * math.sin(x) + math.cos(x)


def f_ctrl(x):
    return math.sqrt(x + 1) - 1 / x


def f_ctrl_dev(x):
    return 1 / math.sqrt(x + 1) + 1 / x**2


def step_calc(a, b, n):
    return (b - a) / n


def LH_rect_method_CONST_h(a, b, n):
    h = step_calc(a, b, n)
    res = 0
    x = a

    while x <= b - h:
        res += f14(x)
        x += h

    res *= h
    return res


def RH_rect_method(a, b, n):
    h = step_calc(a, b, n)
    res = 0
    x = a + h

    while x <= b:
        res += f14(x)
        x += h

    res *= h
    return res


def trapezoid_method(a, b, n):
    h = step_calc(a, b, n)
    res = 0
    x = a + h

    while x <= b - h:
        res += f14(x)
        x += h

    res = h * ((f14(a) + f14(b)) / 2 + res)
    return res


def parabola_method(a, b, n):
    h = step_calc(a, b, n)
    sum_even = 0
    sum_uneven = 0
    x = a + h

    while x <= b - h:
        sum_even += f14(x)
        x += 2 * h

    x = a + 2 * h

    while x <= b - 2 * h:
        sum_uneven += f14(x)
        x += 2 * h

    res = h / 3 * (f14(a) + f14(b) + 4 * sum_even + 2 * sum_uneven)
    return res


def rect_method_remainder(a, b, n, e):
    h = step_calc(a, b, n)
    IN = 0
    I2N = 0
    R = 1

    while R > e:
        S2 = 0
        x = a
        while x <= b - h:
            S2 += f14(x)
            x += h
        I2N = h * S2
        R = abs(I2N - IN)
        IN = I2N
        h = h / 2
    return I2N


def mult_integrals(a, b, c, d, hx, hy):
    sx = 0
    x = a
    while x <= b - hx:
        y = c
        x += hx
        sy = 0
        while y <= d - hy:
            y += hy
            sy += abs(math.sin(x + y))
        Iy = hy * sy
        sx += Iy
    return hx * sx


def newtons_method_ind(a, b, e):
    if f14_2(a) * f14_2(b) > 0:
        res = "Ошибка!- На данном интервале нет корней"
    else:
        ia = 1
        x0 = a
        xa = x0 - f14_2(x0) / f14_2_dev(x0)
        while abs(x0 - xa) > e:
            x0 = xa
            xa = x0 - f14_2(x0) / f14_2_dev(x0)
            ia += 1
        ib = 1
        x0 = b
        xb = x0 - f14_2(x0) / f14_2_dev(x0)
        while abs(x0 - xb) > e:
            x0 = xb
            xb = x0 - f14_2(x0) / f14_2_dev(x0)
            ib += 1
        res = "Результат при a: " + str(xa) + "\nКол-во итераций: " + str(
            ia - 1) + "\nРезультат при b: " + str(
                xb) + "\nКол-во итераций: " + str(ib - 1)
    return res


def newtons_method_ctrl(a, b, e):
    print(a, b, e, f_ctrl(a), f_ctrl(b))
    if f_ctrl(a) * f_ctrl(b) > 0:
        res = "Ошибка! На данном интервале нет корней"
    else:
        ia = 1
        x0 = a
        xa = x0 - f_ctrl(x0) / f_ctrl_dev(x0)
        while abs(x0 - xa) > e:
            x0 = xa
            xa = x0 - f_ctrl(x0) / f_ctrl_dev(x0)
            ia += 1
        ib = 1
        x0 = b
        xb = x0 - f_ctrl(x0) / f_ctrl_dev(x0)
        while abs(x0 - xb) > e:
            x0 = xb
            xb = x0 - f_ctrl(x0) / f_ctrl_dev(x0)
            ib += 1
        res = "Результат при a: " + str(xa) + "\nКол-во итераций: " + str(
            ia - 1) + "\nРезультат при b: " + str(
                xb) + "\nКол-во итераций: " + str(ib - 1)
    return res


def separation_ind(a, b, e):
    i = 0
    x = x1 = x2 = (b - a) / 2
    y = f14_2(x)
    while True:
        x1 += e
        x2 -= e
        y1 = f14_2(x1)
        y2 = f14_2(x2)
        p1 = y * y1
        p2 = y * y2
        if p1 < 0:
            b = x1
            a = b - e
            break
        elif p2 < 0:
            a = x2
            b = a + e
            break
        i += 1
        if a == 1:
            break
    res = "\na: " + str(a) + "\nb: " + str(b) + "\nКол-во итераций: " + str(i)
    return res


def separation_ctrl(a, b, e):
    i = 0
    x1 = x2 = (b - a) / 2
    y = f_ctrl(x1)
    while True:
        x1 += e
        x2 -= e
        y1 = f_ctrl(x1)
        y2 = f_ctrl(x2)
        p1 = y * y1
        p2 = y * y2
        if p1 < 0:
            b = x1
            a = b - e
            break
        elif p2 < 0:
            a = x2
            b = a + e
            break
        i += 1
        if a == 1:
            break
    res = "\na: " + str(a) + "\nb: " + str(b) + "\nКол-во итераций: " + str(i)
    return res


def division_ind(a, b, e):
    i = 1
    while True:
        y = (a + b) / 2
        if f14_2(y) > 0:
            b = y
        else:
            a = y
        i += 1
        if abs(f14_2(y)) <= e:
            break
    res = "Результат: " + str(y) + "\nКол-во итераций: " + str(i)
    return res


def division_ctrl(a, b, e):
    i = 1
    while True:
        y = (a + b) / 2
        if f_ctrl(y) > 0:
            b = y
        else:
            a = y
        i += 1
        if abs(f_ctrl(y)) <= e:
            break
    res = "Результат: " + str(y) + "\nКол-во итераций: " + str(i)
    return res


def chord_ind(a, b, e):
    i = 1
    z = b
    while True:
        f = f14_2(z)
        f0 = f14_2(a)
        z -= f / (f0 - f) * (a - z)
        i += 1
        if abs(f) <= e:
            break
    res = "Результат: " + str(z) + "\nКол-во итераций: " + str(i)
    return res


def chord_ctrl(a, b, e):
    i = 1
    z = b
    while True:
        f = f_ctrl(z)
        f0 = f_ctrl(a)
        z -= f / (f0 - f) * (a - z)
        i += 1
        if abs(f) <= e:
            break
    res = "Результат: " + str(z) + "\nКол-во итераций: " + str(i)
    return res


def calc_eps_func(a, e, x):
    n = 7
    c = 0
    k = 0
    p = 1
    while k <= n:
        p *= x
        u = p * a[k]
        c += u
        k += 1
        if abs(u) <= e:
            res = "c = " + str(c) + ", k = " + str(k - 1)
            break
    if abs(u) > e:
        res = "Требуемая точность не достигнута"
    return res


def calc_sin_func(a, e, x):
    n = 4
    c = 0
    k = 0
    while k <= n:
        p = x**(2 * k + 1)
        u = p * a[2 * k + 1]
        print(u)
        c += u
        k += 1
        if abs(u) <= e:
            res = "c = " + str(c) + ", k = " + str(k - 1)
            break
    if abs(u) > e:
        res = "Требуемая точность не достигнута"
    return res


def iteration_1(x, y0, e):
    y = y0
    r = 1
    while r > e:
        y = (y0 + x / y0) / 2
        r = abs(y - y0)
        y0 = y
    res = "y = " + str(y)
    return res


def iteration_2(x, y0, e):
    y = y0
    r = 1
    while r > e:
        y = y0 / 2 * (3 - x * y0**2)
        r = abs(y - y0)
        y0 = y
    res = "y = " + str(y)
    return res
