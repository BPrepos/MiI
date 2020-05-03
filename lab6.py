import numpy as np
import matplotlib.pyplot as plt
from labgotowe import random
from lab5 import rectangular_kernel
A = 1
N = 500
Z = np.random.normal(0,1,N)
X = 4*random(0.123123421, 13, N)-2
x_sorted = sorted(X)
h_table = [0.5, 1, 1.5, 2]



def m_function(a, x):
    return a*np.tan(a*x)

def system_output(x_tab, z_tab):
    output = []
    for x in range(len(x_tab)):
        output.append(m_function(A, x_tab[x])+z_tab[x])
    return output

def regres_estimator(kernel_type, Y_tab, X_tab):
    x = np.linspace(-2, 2, N)
    output = []
    for i in range(len(x)):
        up = 0
        down = 0
        for n in range(len(X_tab)):
            up += system_output(X_tab[n], Z[n])






if __name__ == "__main__":
    plt.figure(1)
    x1, y1 = x_sorted, m_function(A, x_sorted)
    plt.plot(x1, y1)
    x2, y2 = X, system_output(X, Z)
    plt.plot(x2, y2, ".")
    plt.show()