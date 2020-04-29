from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from labgotowe import random, f4

n = 100000
z = 15
x0 = 0.1423189


def fin1(x):
    if -1 < x <= 0:
        tmp = x + 1
    elif 0 < x <= 1:
        tmp = 1 - x
    else:
        tmp = 0
    return tmp


def fin2(x):
    if 0 < x < 0.01:
        tmp = 50
    elif 0.01 < x <= 1:
        tmp = 50 / 99
    else:
        tmp = 0
    return tmp


def fin4(x):
    tmp = (1 / (2 * np.pi)) * np.exp(-1 * np.power(x, 2) / 2)
    return tmp

def finCauchy(x):
    tmp = 1/(np.pi*(1+pow(x,2)))
    return tmp



def eliminate1(n):
    u2 = random(x0, z, n)
    u1 = 2 * random(1.7231 * x0, z - 2, n) - 1
    list = []
    for i in range(len(u2)):
        if u2[i] <= fin1(u1[i]):
            list.append(u1[i])
    return list


def eliminate2(n):
    u2 = 50 * random(x0, z, n)
    u1 = random(1.7231 * x0, z - 2, n)
    list = []
    for i in range(len(u2)):
        if u2[i] <= fin2(u1[i]):
            list.append(u1[i])
    return list


def eliminate4(n,x00):
    c = sqrt(2*np.e/np.pi)
    V = f4(n)
    U = random(x00,z,n)
    list = []
    for i in range(len(V)):
        if np.fabs(V[i]) <= sqrt(-2*np.log(U[i]))+1:
            list.append(V[i])
    return list
def eliminateCauchy(n):
    u2=0.35*random(0.1423123,13,n)
    u1 = 4*random(0.1221321,11,n)-8
    list = []
    for i in range(len(u2)):
        if u2[i] <= finCauchy(u1[i]):
            list.append(u1[i])
    return list







if __name__ == '__main__':
    X = np.stack(eliminate4(10000,x0))
    #X = np.stack(eliminate4(n,0.1232132131))
    print(X)
    plt.hist(X, bins='auto')
    plt.show()
