import numpy as np
import matplotlib.pyplot as plt
from labgotowe import random
from lab5 import rectangular_kernel, epanechnikov_kernel, boscar_kernel
A = 1
N = 500
Z = np.random.normal(0,1,N)
X = 4*random(0.14123216, 15, N)-2
x_sorted = sorted(X)
Q = 100



def m_function(a, x):
    return np.arctan(a * x)

def m_function_all(a, tab):
    output = []
    for i in range(len(tab)):
        output.append(m_function(a, tab[i]))
    return output


def system_output(x_tab, z_tab):
    output = []
    for x in range(len(x_tab)):
        output.append(m_function(A, x_tab[x])+z_tab[x])
    return output


def valid(kernel_type, x_tab, y_tab, hv):
    tmp = 0
    for q in range(2*Q):
        tmp += 1/(2*Q) * pow(regres_for_single(kernel_type, x_tab, y_tab, hv, (q-Q)/Q)-m_function(A, (q-Q)/Q), 2)
    return tmp

def valid_for_multiple(xtab, ytab):
    htab = np.linspace(0.1, 2, 20)
    tmp = []
    for it in htab:
        tmp.append(valid("rectangular", xtab, ytab, it))
    return htab, tmp


def regres_estimator(kernel_type, X_tab, Y_tab, hn):
    x = np.linspace(-2, 2, N)
    m_ret = []
    for i in range(len(x)):
        up = 0
        down = 0
        for n in range(len(X_tab)):
            if kernel_type == "rectangular":
                up += Y_tab[n] * rectangular_kernel((X_tab[n]-x[i])/hn)
                down += rectangular_kernel((X_tab[n]-x[i])/hn)
            elif kernel_type == "boscar":
                up += Y_tab[n] * boscar_kernel((X_tab[n]-x[i])/hn)
                down += boscar_kernel((X_tab[n]-x[i])/hn)
            elif kernel_type == "epan":
                up += Y_tab[n] * epanechnikov_kernel((X_tab[n]-x[i])/hn)
                down += epanechnikov_kernel((X_tab[n]-x[i])/hn)
        m_ret.append(up/down)
    return x, m_ret

def regres_for_single(kernel_type, X_tab, Y_tab, hn, x):
    up = 0
    down = 0
    for n in range(len(X_tab)):
        if kernel_type == "rectangular":
            up += Y_tab[n] * rectangular_kernel((X_tab[n]-x)/hn)
            down += rectangular_kernel((X_tab[n]-x)/hn)
        elif kernel_type == "boscar":
            up += Y_tab[n] * boscar_kernel((X_tab[n]-x)/hn)
            down += boscar_kernel((X_tab[n]-x)/hn)
        elif kernel_type == "epan":
            up += Y_tab[n] * epanechnikov_kernel((X_tab[n]-x)/hn)
            down += epanechnikov_kernel((X_tab[n]-x)/hn)
    return up/down






if __name__ == "__main__":
    plt.figure(1)
    x1, y1 = x_sorted, m_function_all(A, x_sorted)
    plt.plot(x1, y1)
    x2, y2 = X, system_output(X, Z)
    plt.plot(x2, y2, ".")
    fig2, ax2 = plt.subplots(3)
    ytab = system_output(X, Z)
    x3, y3 = regres_estimator("rectangular", X, ytab, 0.1)
    ax2[0].plot(x3, y3)
    ax2[0].plot(x1, y1)
    ax2[0].set_title('h = 0.1')
    x4, y4 = regres_estimator("rectangular", X, ytab, 0.6)
    ax2[1].plot(x4, y4)
    ax2[1].plot(x1, y1)
    ax2[1].set_title('h = 0.6')
    x5, y5 = regres_estimator("rectangular", X, ytab, 2.8)
    ax2[2].plot(x5, y5)
    ax2[2].plot(x1, y1)
    ax2[2].set_title('h = 2.8')
    # lets set
    h = 0.9
    fig3, ax3 = plt.subplots(3)
    x6, y6 = regres_estimator("rectangular", X, ytab, h)
    x7, y7 = regres_estimator("boscar", X, ytab, h)
    x8, y8 = regres_estimator("epan", X, ytab, h)
    ax3[0].plot(x6,y6)
    ax3[0].plot(x1, y1)
    ax3[0].set_title('jądro prostokątne')
    ax3[1].plot(x7,y7)
    ax3[1].plot(x1, y1)
    ax3[1].set_title('jądro boscar')
    ax3[2].plot(x8, y8)
    ax3[2].plot(x1, y1)
    ax3[2].set_title('jądro epanechnikova')
    #DO for other a
    plt.figure(4)
    #x9, y9 = valid_for_multiple(X, ytab)
    #plt.plot(x9,y9)


    plt.show()

