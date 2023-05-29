import concurrent.futures as ftres
from functools import partial
from cython.parallel import prange

def integrate(f, a, b, *, n_iter=10000):
    try:
        if a > b:
            a, b = b, a

        h = (b - a) / n_iter
        s = 0.5 * (f(a) + f(b))
        for i in range(1, n_iter):
            s += f(a + i * h)
        return h * s
    except ValueError:
        return "Ошибка. Скорее всего, интеграл невозможно вычислить на данном промежутке."

def async_integrate(f, a, b, *, n_iter=1000000):
    n_jobs = 4
    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs)
    step = (b - a) / n_jobs

    fs = [(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]

    spawn_lst = []
    for i in fs:
        spawn = partial(executor.submit, integrate, f, i[0], i[1])
        spawn_lst.append(spawn)

    res = []
    for f in spawn_lst:
        res.append(f())

    s = [r.result() for r in ftres.as_completed(res)]

    return sum(s)
