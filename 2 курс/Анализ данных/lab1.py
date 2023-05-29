d1 = 14.85
d2 = 14.8
d3 = 14.79
d4 = 14.84
d5 = 14.81
d0 = 14.8
d_average = d0 + 1 / 5 * (d1 - d0 + d2 - d0 + d3 - d0 + d4 - d0 + d5 - d0)
dispersion = 1 / (5 * (5 - 1)) * ((pow(d1 - d0, 2) + pow(d2 - d0, 2) +
                                   pow(d3 - d0, 2) + pow(d4 - d0, 2) +
                                   pow(d5 - d0, 2)) -
                                  5 * pow(d_average - d0, 2))

standard_deviation = pow(dispersion, 0.5)
absolute_error = 2.57 * standard_deviation
relative_error = absolute_error / d_average * 100

print("В результате определения диаметра цилиндра получены следующие значени"
      "я (в мм):\n14.85, 14.8, 14.79, 14.84, 14.81.\nd_0 = 14.8, а d_среднее"
      " = " + str(d_average) + ".\n\nСредне-квадратичная погрешность = " +
      str(dispersion) + ".\nСтандартное отклонение = " +
      str(standard_deviation) + ".\nАбсолютная погрешность = " +
      str(absolute_error) + ".\nОтносительная погрешность = " +
      str(relative_error) + ".")
