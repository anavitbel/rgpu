from PyQt5 import uic

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import calculations as calc

Form, Window = uic.loadUiType("MainWindow.ui")
Form1, Window1 = uic.loadUiType("Task1Window.ui")
Form2, Window2 = uic.loadUiType("Task2Window.ui")
Form3, Window3 = uic.loadUiType("Task3Window.ui")
Form4, Window4 = uic.loadUiType("Task4Window.ui")
Form5, Window5 = uic.loadUiType("Task5Window.ui")


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

window4 = Window4()
form4 = Form4()
form4.setupUi(window4)


window5 = Window5()
form5 = Form5()
form5.setupUi(window5)


def update_graph(coor_x, coor_y, self):
    self.MplWidget.canvas.axes.clear()
    self.MplWidget.canvas.axes.plot(coor_x, coor_y)
    self.MplWidget.canvas.axes.set_title('График')
    self.MplWidget.canvas.draw()


def open_task1():
    window.close()
    window1.show()


def open_task2():
    window.close()
    window2.show()


def open_task3():
    window.close()
    window3.show()


def open_task4():
    window.close()
    window4.show()


def open_task5():
    window.close()
    window5.show()


def task1_euler():
    a = float(form1.ds_a.value())
    b = float(form1.ds_b.value())
    n = int(form1.sb_n.value())
    x = float(form1.ds_x.value())
    y = float(form1.ds_y.value())
    form1.ds_h.setValue(calc.step_calc(a, b, n))

    res = calc.euler1(lambda x, y: y * (1 - x), x, y, a, b, n)
    coor_x = res[:int(len(res) / 2)]
    coor_y = res[int(len(res) / 2):]

    rowPosition = form1.tableW.rowCount()
    for i in list(reversed(range(0, rowPosition))):
        form1.tableW.removeRow(i)

    for i in range(0, len(coor_x)):
        rowPosition = form1.tableW.rowCount()
        form1.tableW.insertRow(rowPosition)
        form1.tableW.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(coor_x[i])))
        form1.tableW.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(coor_y[i])))

    update_graph(coor_x, coor_y, form1)


def task2_euler():
    a = float(form2.ds_a.value())
    b = float(form2.ds_b.value())
    h = float(form2.ds_h.value())
    y0 = float(form2.ds_y.value())
    y1 = float(form2.ds_y_der.value())

    res = calc.euler2(a, b, h, y0, y1)

    coor_x = list(map(calc.round_func, res['x']))
    coor_y = list(map(calc.round_func, res['y']))
    coor_z = list(map(calc.round_func, res['z']))

    rowPosition = form2.tableW.rowCount()
    for i in list(reversed(range(rowPosition))):
        form2.tableW.removeRow(i)

    for i in range(len(coor_x)):
        rowPosition = form2.tableW.rowCount()
        form2.tableW.insertRow(rowPosition)
        form2.tableW.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(coor_x[i])))
        form2.tableW.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(coor_y[i])))
        form2.tableW.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(coor_z[i])))
    update_graph(coor_x, coor_y, form2)


def task3_euler():
    a = float(form3.ds_a.value())
    b = float(form3.ds_b.value())
    h = float(form3.ds_h.value())
    x0 = float(form3.ds_x.value())
    y0 = float(form3.ds_y.value())
    z0 = float(form3.ds_z.value())

    res = calc.euler3(a, b, h, x0, y0, z0)
    x = list(map(calc.round_func, res['x']))
    y = list(map(calc.round_func, res['y']))
    z = list(map(calc.round_func, res['z']))
    t = list(map(calc.round_func, res['t']))

    rowPosition = form3.tableW.rowCount()
    for i in list(reversed(range(rowPosition))):
        form3.tableW.removeRow(i)

    for i in range(len(x)):
        rowPosition = form3.tableW.rowCount()
        form3.tableW.insertRow(rowPosition)
        form3.tableW.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(t[i])))
        form3.tableW.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(x[i])))
        form3.tableW.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(y[i])))
        form3.tableW.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(z[i])))


def task4_euler():
    t0 = float(form4.ds_t.value())
    ts = float(form4.ds_ts.value())
    r = float(form4.ds_r.value())
    h = float(form4.ds_h.value())
    time_max = float(form4.ds_time_max.value())

    res = calc.coffee_temp(t0, ts, r, h, time_max)
    t = res['t']
    time = res['time']
    update_graph(time, t, form4)
    t_optima = "не успеет"
    for i in range(len(t)):
        if t[i] < 50:
            t_optima = round(time[i])
            break
    form4.lSec.setText(f'{t_optima}')


def task5_euler():
    e = int(form5.sb_E.value())
    r = int(form5.sb_R.value())
    l = int(form5.sb_L.value())
    h = float(form5.ds_h.value())
    time_max = float(form5.ds_time_max.value())

    res = calc.el_curcuit(e, r, l, h, time_max)
    current = res['I']
    time = res['time']
    update_graph(time, current, form5)
    t_optima = "n/a"
    for i in range(len(time)):
        if current[i] > 0.98:
            t_optima = time[i]
            break
    form5.lSec.setText(f'{t_optima}')

def task1_RG():
    a = float(form1.ds_a.value())
    b = float(form1.ds_b.value())
    n = int(form1.sb_n.value())
    x = float(form1.ds_x.value())
    y = float(form1.ds_y.value())
    form1.ds_h.setValue(calc.step_calc(a, b, n))

    res = calc.rg1(lambda x, y: y * (1 - x), x, y, a, b, n)
    coor_x = res[:int(len(res) / 2)]
    coor_y = res[int(len(res) / 2):]

    rowPosition = form1.tableW_2.rowCount()
    for i in list(reversed(range(0, rowPosition))):
        form1.tableW_2.removeRow(i)

    for i in range(0, len(coor_x)):
        rowPosition = form1.tableW_2.rowCount()
        form1.tableW_2.insertRow(rowPosition)
        form1.tableW_2.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(coor_x[i])))
        form1.tableW_2.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(coor_y[i])))

    update_graph(coor_x, coor_y, form1)


def return_from_task1():
    window1.close()
    window.show()


def return_from_task2():
    window2.close()
    window.show()


def return_from_task3():
    window3.close()
    window.show()


def return_from_task4():
    window4.close()
    window.show()

def return_from_task5():
    window5.close()
    window.show()


form.TaskButton1.clicked.connect(open_task1)
form.TaskButton2.clicked.connect(open_task2)
form.TaskButton3.clicked.connect(open_task3)
form.TaskButton4.clicked.connect(open_task4)
form.TaskButton5.clicked.connect(open_task5)

form1.bEuler.clicked.connect(task1_euler)
form1.bRG.clicked.connect(task1_RG)
form1.bReturn.clicked.connect(return_from_task1)

form2.bEuler.clicked.connect(task2_euler)
form2.bReturn.clicked.connect(return_from_task2)

form3.bEuler.clicked.connect(task3_euler)
form3.bReturn.clicked.connect(return_from_task3)

form4.bEuler.clicked.connect(task4_euler)
form4.bReturn.clicked.connect(return_from_task4)


form5.bEuler.clicked.connect(task5_euler)
form5.bReturn.clicked.connect(return_from_task5)

app.exec_()
