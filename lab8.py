import numpy as np
import matplotlib.pyplot as plt
from labgotowe import random

D = 10
N = 200
L = 10
var = 1
tab_n = np.linspace(16, 100, 42).astype(int)


if __name__ == "__main__":
    #generate a
    a = np.zeros(D)
    for i in range(D):
        a[i] = 1
    #generate Xn
    Xn = np.zeros((N, 10), dtype=float)
    for i in range(100):
        for j in range(D):
            Xn[i][j] = np.random.normal(0, 1)
    #generate Zn
    Zn = np.zeros(N)
    for i in range(len(Zn)):
        Zn[i] = np.random.normal(0, var)
    #calculate Yn
    Yn = np.add(Xn.dot(a), Zn)
    #estimate a
    a_est = np.dot(np.dot(np.linalg.inv(np.dot(Xn.transpose(),Xn)),Xn.transpose()),Yn)
    #error
    #cov
    cov = var * np.linalg.inv(np.dot(Xn.transpose(),Xn))
    plt.pcolormesh(cov)
    error_tab = []
    Zn = np.zeros((L,N))
    for l in range(L):
        for i in range(N):
            Zn[l][i] = np.random.normal(0, var)
    for n in tab_n:
        x_tmp = Xn[:n,:]
        error = 0
        for l in range(L):
            z_tmp = Zn[l][:n]
            y_tmp = np.add(x_tmp.dot(a), z_tmp)
            a_estimated_tmp = np.dot(np.dot(np.linalg.inv(np.dot(x_tmp.transpose(),x_tmp)),x_tmp.transpose()),y_tmp)
            error += 1/L * pow((np.linalg.norm(a_estimated_tmp-a)),2)
        error_tab.append(error)
    print(error_tab)
    plt.figure(2)
    plt.plot(tab_n, error_tab)
    plt.show()





