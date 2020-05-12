import numpy as np
import matplotlib.pyplot as plt
from labgotowe import random

D = 10
N = 100


if __name__ == "__main__":
    #generate a
    a = np.zeros(D)
    for i in range(D):
        a[i] = 1
    #generate Xn
    Xn = np.zeros((100, 10), dtype=float)
    for i in range(100):
        for j in range(D):
            Xn[i][j] = np.random.normal(0, 1)
    #generate Zn
    Zn = np.zeros(N)
    for i in range(len(Zn)):
        Zn[i] = np.random.normal(0, 1)
    #calculate Yn
    Yn = np.add(Xn.dot(a), Zn)
    print(Yn)



