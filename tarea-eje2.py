import pandas as pd
import pathlib


x0 = 1.4  # Semilla
n = 5


def xn(x, numero_repeticiones):

    valores_xn = []
    xn_formateados_8_decimales = []

    for i in range(numero_repeticiones):

        y = x-(((x**5-(3*x**4)+(3*x**3)-(3*x**2)-x+6)) /
               ((5*x**4)-(12*x**3)+(9*x**2)-(6*x)-1))
        valores_xn.append(x)
        xn_formateados_8_decimales.append(f"{x:.8}")
        x = y
    return [valores_xn, xn_formateados_8_decimales]


def fxn(xn):
    fxn_values = []

    for x in xn:
        # Funcion Original
        y = (x**5-(3*x**4)+(3*x**3)-(3*x**2)-x+6)
        fxn_values.append(f"{y:.8}")

    return fxn_values


def f_derivate(xn):
    f_derivate_values = []

    for x in xn:
        # Funcion derivada
        y = ((5*x**4)-(12*x**3)+(9*x**2)-(6*x)-1)
        f_derivate_values.append(f"{y:.8}")

    return f_derivate_values


def xn_noformat(x, numero_repeticiones):
    values = []

    for i in range(numero_repeticiones):

        y = x-(((x**5-(3*x**4)+(3*x**3)-(3*x**2)-x+6) /
                ((5*x**4)-(12*x**3)+(9*x**2)-(6*x)-1)))

        x = y
        values.append(f"{x:.8}")
    return values


def accuary(xn):
    values = ["-"]
    for i in range(len(xn)):
        if i < len(xn)-1:
            values.append(f"{float(abs(xn[i+1]-xn[i])):.8}")
    return values


x_values = xn(x0, n)

fxn = fxn(x_values[0])

fderiva = f_derivate(x_values[0])

xn_nformt = xn_noformat(x0, n)

acc = accuary(x_values[0])


table = [x_values[1], fxn, fderiva, xn_nformt, acc]
df = pd.DataFrame(table).T


df.to_excel(excel_writer=((str(pathlib.Path().parent.absolute()
                               ).replace("\\", "/")+"/Newton_Raphson.xlsx")))
