import math
from decimal import Decimal


def func_1(x, y):
    return y * (1 - x)


def step_calc(a, b, n):
    return (b - a) / n


def round_func(x):
    x = Decimal(f"{x}")
    x = float(x.quantize(Decimal("1.00000")))
    return x


def euler1(f, x, y, a, b, n):
    h = step_calc(a, b, n)
    res1 = []
    res2 = []
    while x < b - h:
        res1.append(round_func(x))
        res2.append(round_func(y))
        y = y + h * f(x, y)
        x += h
    res = res1 + res2
    return res


def rg1(f, x, y, a, b, n):
    h = step_calc(a, b, n)
    res1 = [x]
    res2 = [y]
    while x < b - h:
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y += k
        x, y = round_func(x + h), round_func(y)
        res1.append(x)
        res2.append(y)
    res = res1 + res2
    return res


def euler2(a, b, h, y, z):
    x = a
    res_x = [x]
    res_y = [y]
    res_z = [z]
    i = 1
    while res_x[i - 1] < b - h:
        res_y.append(res_y[i - 1] + res_z[i - 1] * h)
        res_z.append(res_z[i - 1] - h * (res_z[i - 1] / res_x[i - 1] + res_y[i - 1]))
        res_x.append(round_func(res_x[i - 1] + h))
        i += 1

    for i in range(len(res_x)):
        res_y[i] = round_func(res_y[i])
        res_z[i] = round_func(res_z[i])
    res = {'x': res_x, 'y': res_y, 'z': res_z}
    return res


def euler3(a, b, h, x0, y0, z0):
    t = [a]
    x = [x0]
    y = [y0]
    z = [z0]
    i = 0
    while t[i] < b - h:
        x.append(x[i] + h * (-2 * x[i] + 5 * z[i]))
        y.append(y[i] + h * (math.sin(t[i] - 1) * x[i] - y[i] + 3 * z[i]))
        z.append(z[i] + h * (-1 * x[i] + 2 * z[i]))
        t.append(round_func(t[i] + h))
        i += 1
    res = {'t': t, 'x': x, 'y': y, 'z': z}
    return res


def coffee_temp(t, ts, r, h, time_max):
    n = int(time_max / h)
    tmpr = [t] * n
    time = [0] * n
    for i in range(len(tmpr) - 1):
        tmpr[i + 1] = round_func(tmpr[i] + h * r * (tmpr[i] - ts))
        time[i + 1] = round_func(time[i] + h)
    res = {'t': tmpr, 'time': time}
    return res


def el_curcuit(e, r, l, h, time_max):
    n = int(time_max / h)
    time = [0] * n
    I = [0] * n
    for i in range(len(time) - 1):
        I[i + 1] = round_func(I[i] + h * (l / (e - r * I[i])))
        time[i + 1] = time[i] + h
    res = {'I': I, 'time': time}
    return res
