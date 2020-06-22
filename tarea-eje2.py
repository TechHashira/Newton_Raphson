import pandas as pd
import pathlib


x0 = 1.4  # Semilla


def xn(x):

    values = []
    for i in range(25):

        y = x-(((x**5-(3*x**4)+(3*x**3)-(3*x**2)-x+6)) / \
            ((5*x**4)-(12*x**3)+(9*x**2)-(6*x)-1))

        values.append(x)
        x = y

    return values


def fxn(xn):
    fxn_values = []
    for x in xn:
        # Funcion Original
        y = (x**5-(3*x**4)+(3*x**3)-(3*x**2)-x+6)
        fxn_values.append(y)

    return fxn_values


def f_derivate(xn):
    f_derivate_values = []
    for x in xn:
        # Funcion derivada
        y = ((5*x**4)-(12*x**3)+(9*x**2)-(6*x)-1)
        f_derivate_values.append(y)

    return f_derivate_values


def xn_noformat(x):
    values = []
    for i in range(25):

        y = x-(((x**5-(3*x**4)+(3*x**3)-(3*x**2)-x+6) /
                ((5*x**4)-(12*x**3)+(9*x**2)-(6*x)-1)))

        values.append(y)
        x = y
    return values


def accuary(xn):
    values = ["-"]
    for i in range(len(xn)):
        if i < len(xn)-1:

            values.append(float(abs(xn[i+1]-xn[i])))
    return values


x_values = xn(x0)
fxn = fxn(x_values)
fderiva = f_derivate(x_values)
xn_nformt = xn_noformat(x0)
acc = accuary(x_values)


table = [x_values, fxn, fderiva, xn_nformt, acc]
df = pd.DataFrame(table).T


df.to_excel(excel_writer=((str(pathlib.Path().parent.absolute()
                               ).replace("\\", "/")+"/Newton_Raphson.xlsx")))
