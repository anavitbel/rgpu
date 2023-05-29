from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
import calculations as calc
import math

Form, Window = uic.loadUiType("MainWindow.ui")
Form1, Window1 = uic.loadUiType("Task1Window.ui")
Form2, Window2 = uic.loadUiType("Task2Window.ui")
Form3, Window3 = uic.loadUiType("Task3Window.ui")
Form3_2, Window3_2 = uic.loadUiType("Task3_2Window.ui")
Form4, Window4 = uic.loadUiType("Task4Window.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

window1 = Window1()
form1 = Form1()
form1.setupUi(window1)

window2 = Window2()
form2 = Form2()
form2.setupUi(window2)

window3 = Window3()
form3 = Form3()
form3.setupUi(window3)

window3_2 = Window3_2()
form3_2 = Form3_2()
form3_2.setupUi(window3_2)

window4 = Window4()
form4 = Form4()
form4.setupUi(window4)


def open_Task1():
    window.close()
    window1.show()


def open_Task2():
    window.close()
    window2.show()


def open_Task3():
    window.close()
    window3.show()


def open_Task3_2():
    window3.close()
    window3_2.show()


def open_Task3_1():
    window3_2.close()
    window3.show()


def open_Task4():
    window.close()
    window4.show()


def task1_calc():
    u_method = form1.comboBMethod.currentText()
    u_algorithm = form1.comboBAlgorithm.currentText()
    u_n = form1.spinN.value()
    a = 0.5
    b = 1.3
    e = 10**(-6)
    res = 0
    if u_algorithm == 'С постоянным шагом':
        if u_method == 'Метод левых прямоугольников':
            res = calc.LH_rect_method_CONST_h(a, b, u_n)
        elif u_method == 'Метод правых прямоугольников':
            res = calc.RH_rect_method(a, b, u_n)
        elif u_method == 'Метод трапеций':
            res = calc.trapezoid_method(a, b, u_n)
        elif u_method == 'Метод парабол':
            res = calc.parabola_method(a, b, u_n)
        else:
            res = 'Введён неверный метод'
    elif u_algorithm == 'С переменным шагом':
        if u_method == 'Метод левых прямоугольников':
            res = calc.rect_method_remainder(a, b, u_n, e)
        else:
            res = 'Алгоритм с переменным шагом \nможет быть выполнен только по методу \nлевых прямоугольников'
    else:
        res = 'Введён неверный алгоритм'

    form1.lOutputRes.setText(f'{res}')


def task2_calc():
    u_nx = form2.sbn_x.value()
    u_ny = form2.sbn_y.value()
    a = 0
    c = 0
    b = math.pi / 2
    d = math.pi / 2
    hx = calc.step_calc(a, b, u_nx)
    hy = calc.step_calc(c, d, u_ny)
    form2.dsh_x.setValue(hx)
    form2.dsh_y.setValue(hy)
    form2.lResult.setText(f'{calc.mult_integrals(a, b, c, d, hx, hy)}')


def task3_eps_calc():
    a = []
    a.append(form3.DSA0_eps.value())
    a.append(form3.DSA1_eps.value())
    a.append(form3.DSA2_eps.value())
    a.append(form3.DSA3_eps.value())
    a.append(form3.DSA4_eps.value())
    a.append(form3.DSA5_eps.value())
    a.append(form3.DSA6_eps.value())
    a.append(form3.DSA7_eps.value())
    e = int(form3.eps_coef_eps.text()) * 10**int(form3.power_of_ten_eps.text())
    x = form3.DSX_eps.value()
    form3.lResult_eps.setText(f'{calc.calc_eps_func(a, e, x)}')


def task3_sin_calc():
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a[1] = form3.DSA1_sin.value()
    a[3] = form3.DSA3_sin.value()
    a[5] = form3.DSA5_sin.value()
    a[7] = form3.DSA7_sin.value()
    a[9] = form3.DSA9_sin.value()
    e = int(form3.eps_coef.text()) * 10**int(form3.power_of_ten_sin.text())
    x = int(form3.pi_coef.text()) * math.pi / int(form3.inverse_pi_coef.text())
    form3.lResult_sin.setText(f'{calc.calc_sin_func(a, e, x)}')


def task3_2_calc():
    e = int(form3_2.eps_coef.text()) * 10**int(form3_2.power_of_ten.text())
    x = form3_2.DSX.value()
    y0 = form3_2.DSY.value()
    form3_2.lResult.setText(f'{calc.iteration_1(x, y0, e)}')


def task3_2_calc_2():
    e = float(form3_2.eps_coef_2.text()) * 10**int(
        form3_2.power_of_ten_2.text())
    x = float(form3_2.DSX_2.value())
    y0 = float(form3_2.DSY_2.value())
    form3_2.lResult_2.setText(f'{calc.iteration_2(x, y0, e)}')

"""
def task4_calc():
    ex = form4.CBExample.currentText()
    method = form4.CBMethod.currentText()
    e = int(form4.eps_coef.text()) * 10**int(form4.power_of_ten.text())
    if ex == "Индивидуальный пример":
        a = form4.dsh_a.value() * math.pi
        b = form4.dsh_b.value() * math.pi
        if method == "Метод касательных":
            form4.lResult.setText(f"{calc.newtons_method_ind(a, b, e)}")
        elif method == "Деление отрезка пополам":
            form4.lResult.setText(f"{calc.separation_ind(a, b, e)}")
        elif method == "Отделение корней уравнения":
            form4.lResult.setText(f"{calc.division_ind(a, b, e)}")
        else:
            form4.lResult.setText(f"{calc.chord_ind(a, b, e)}")
    elif ex == "Контрольный пример":
        a = form4.dsh_a.value()
        b = form4.dsh_b.value()
        if method == "Метод касательных":
            form4.lResult.setText(f"{calc.newtons_method_ctrl(a, b, e)}")
        elif method == "Деление отрезка пополам":
            form4.lResult.setText(f"{calc.division_ctrl(a, b, e)}")
        elif method == "Отделение корней уравнения":
            form4.lResult.setText(f"{calc.separation_ctrl(a, b, e)}")
        else:
            form4.lResult.setText(f"{calc.chord_ctrl(a, b, e)}")

"""
def return_from_Task1():
    window1.close()
    window.show()


def return_from_Task2():
    window2.close()
    window.show()


def return_from_Task3():
    window3.close()
    window.show()


def return_from_Task3_2():
    window3_2.close()
    window.show()

"""
def return_from_Task4():
    window4.close()
    window.show()


def show_Example():
    if form4.CBExample.currentText() == "Контрольный пример":
        form4.label.setPixmap(QPixmap("ctrlTask4.png"))
        form4.pi_a.setText("")
        form4.pi_b.setText("")
        form4.dsh_a.setValue(0.5)
        form4.dsh_b.setValue(1)
    elif form4.CBExample.currentText() == "Индивидуальный пример":
        form4.label.setPixmap(QPixmap("individTask4.png"))
        form4.pi_a.setText("* π")
        form4.pi_b.setText("* π")
        form4.dsh_a.setValue(-2)
        form4.dsh_b.setValue(2)
    else:
        form4.label.setPixmap(QPixmap(""))
        form4.pi_a.setText("")
        form4.pi_b.setText("")
        form4.dsh_a.setValue(0)
        form4.dsh_b.setValue(0)

"""
form.TaskButton1.clicked.connect(open_Task1)
form.TaskButton2.clicked.connect(open_Task2)
form.TaskButton3.clicked.connect(open_Task3)
form.TaskButton4.clicked.connect(open_Task4)
"""
form1.bCalculation.clicked.connect(task1_calc)
form1.bReturn.clicked.connect(return_from_Task1)
"""
form2.bCalculation.clicked.connect(task2_calc)
form2.bReturn.clicked.connect(return_from_Task2)

form3.bCalculation_eps.clicked.connect(task3_eps_calc)
form3.bCalculation_sin.clicked.connect(task3_sin_calc)
form3.bReturn.clicked.connect(return_from_Task3)
form3.bPart2.clicked.connect(open_Task3_2)

form3_2.bCalculation.clicked.connect(task3_2_calc)
form3_2.bCalculation_2.clicked.connect(task3_2_calc_2)
form3_2.bReturn.clicked.connect(return_from_Task3_2)
form3_2.bPart1.clicked.connect(open_Task3_1)
"""
form4.CBExample.activated.connect(show_Example)
form4.bCalculation.clicked.connect(task4_calc)
form4.bReturn.clicked.connect(return_from_Task4)
"""
app.exec_()
