from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import random


def random(x0,z,n):#generacja liczb losowych z rozkładu jednostajnego
    x = np.zeros((n+1,1))
    x[0]=x0
    for i in range(n):
        x[i+1]=z*x[i]-np.floor(z*x[i])
    return x[1:n+1]
def f1(n):#generacja liczb losowych z rozkładu trójkątnego (zadanie 1 instrukcja 1)
    u = random(0.12341233124,13,n)
    return np.sqrt(u)
def f2(n):
    u = random(0.12341233124, 13, n)
    for i in range(len(u)):
        if 0 < u[i] < 0.5:
            u[i] = -1 + sqrt(2 * u[i])
        elif 0.5 <= u[i] < 1:
            u[i] = 1 + sqrt(2 * u[i])
        else:
            u[i] = 0
    return u
def f3(n):#generacja liczn losowych z rozkładu wykładniczego
    u = random(0.12341233124,13,n)
    return -np.log(u)
def f4(n):
    u = random(0.12341233124, 13, n)
    for i in range(len(u)):
        if 0 <= u[i] < 0.5:
            u[i] = -np.log(1+2*(u[i]-0.5))
        elif 0.5 <= u[i] <= 1:
            u[i] = np.log(1-2*(u[i]-0.5))
    return u
if __name__ == '__main__':
    n = 100000
    x0 = 0.141223
    z = 15
    plt.figure(1)
    x = f1(n)
    plt.hist(x, bins='auto')
    plt.figure(2)
    x = f2(n)
    plt.hist(x, bins='auto')
    plt.figure(3)
    x = f3(n)
    plt.hist(x, bins='auto')
    plt.figure(4)
    x = f4(n)
    plt.hist(x, bins='auto')
    # plt.figure(5)
    # plt.title("Histogram dla z=15, x0=0.141223")
    # x = random(x0,z,n)
    # print(x)
    # plt.hist(x,bins='auto')
    plt.show()
    #
