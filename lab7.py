import numpy as np
import matplotlib.pyplot as plt
from labgotowe import random
from lab5 import rectangular_kernel, epanechnikov_kernel, boscar_kernel

A = 1
N= 250
L = 15
Q = 100
x_tab = 2* np.pi * random(0.14123141, 15, N) - np.pi
x_sorted = sorted(x_tab)
z_tab = np.random.normal(0, 1, 500)


def m7_function(a, x):
    if 0 <= abs(x) < 1:
        tmp = a*pow(x,2)
    elif 1 <= abs(x) < 2:
        tmp = 1
    else:
        tmp = 0
    return tmp


def m7_for_tab(a, tab):
    output = []
    for i in range(len(tab)):
        output.append(m7_function(a, tab[i]))
    return output

def system_output(x_tab, z_tab):
    output = []
    for x in range(len(x_tab)):
        output.append(m7_function(A, x_tab[x])+z_tab[x])
    return output

def fi(k, x):
    if k ==0:
        return np.sqrt(1/(2*np.pi))
    else:
        return np.sqrt(1/np.pi)*np.cos(k*x)

def est_m(g, f):
    if f == 0:
        return 0
    else:
        return g/f


def est_m_for_single(tabx, taby, x):
    g = 0
    f = 0
    for k in range(L):
        beta = 0
        alfa = 0
        for n in range(len(tabx)):
            tmp = 1/N * fi(k, tabx[n])
            beta += tmp
            alfa += tmp * taby[n]
        g += alfa * fi(k, x)
        f += beta * fi(k, x)
    return est_m(g,f)


def est_m_for_all(tabx, taby):
    output = []
    x = np.linspace(-np.pi, np.pi, 100)
    for i in range(len(x)):
        g = 0
        f = 0
        for k in range(L):
            beta = 0
            alfa = 0
            for n in range(len(tabx)):
                tmp = 1/N * fi(k, tabx[n])
                beta += tmp
                alfa += tmp * taby[n]
            g += alfa * fi(k, x[i])
            f += beta * fi(k, x[i])
        output.append(est_m(g,f))
    return x, output

def valid(x_tab, y_tab):
    tmp = 0
    for q in range(2*Q):
        arg = (2*q - 2*Q)/Q
        tmp += 1/(2*Q) * pow(est_m_for_single(x_tab, y_tab, arg)-m7_function(A, arg), 2)
    return tmp





if __name__ == "__main__":
    x_lin = np.linspace(-np.pi, np.pi, 500)
    y_lin = m7_for_tab(A, x_lin)
    y_tab = m7_for_tab(A, x_sorted)
    plt.figure(1)
    plt.plot(x_lin, y_lin)
    plt.plot(x_tab, system_output(x_tab, z_tab), ".")
    plt.figure(2)
    x1, y1 = est_m_for_all(x_sorted, y_tab)
    plt.plot(x1, y1)
    plt.plot(x_lin, y_lin)
    plt.title('L = 15')
    Ltab = np.linspace(5, 50, 10).astype(int)
    Ntab = np.linspace(25, 250, 10).astype(int)
    final = []
    #for i in range(len(Ltab)):
     #   L = Ltab[i]
      #  N = Ntab[i]
       # final.append(valid(x_sorted, y_tab,))
    #plt.figure(3)
    #plt.plot(Ltab, final)
    plt.show()
