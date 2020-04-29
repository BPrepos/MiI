from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from labgotowe import random
from lab2 import eliminate4, z, x0, eliminateCauchy

x0list = [0.29, 0.142321, 0.23, 0.512, 0.432, 0.42, 0.25, 0.65, 0.43, 0.23]
x0list2 = [0.29, 0.142321, 0.23, 0.512, 0.432, 0.42, 0.25, 0.65, 0.43, 0.23,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2321,0.21]
nlist = [5, 10,20,50,70,90, 100,150,250, 300, 500, 800, 1000,2000]


def est_mi(X):
    mi = 0
    for i in range(len(X)):
        mi += (1 / len(X)) * X[i]
    return mi


def s2n(X, mi):
    s = 0
    for i in range(len(X)):
        s += 1 / len(X) * pow((X[i] - mi), 2)
    return s


def S2N(X, mi):
    s = 0
    for i in range(len(X)):
        s += pow((X[i] - mi), 2)
    return s / (len(X) - 1)


def estmi_for_T(par_list,n):
    tmplist = []
    foo = 0
    for i in range(len(par_list)):
        foo = est_mi(eliminate4(n,par_list[i]))
        tmplist.append(foo)
    return tmplist

def error_for_1N(estmilist):
    err = 0
    for i in range(len(estmilist)):
        err += 1/len(estmilist)*pow(estmilist[i]-0,2)
    return err

def ests2_for_T(par_list,n):
    tmplist = []
    foo = 0
    for i in range(len(par_list)):
        foo = S2N(eliminate4(n,par_list[i]),0)
        tmplist.append(foo)
    return tmplist

def errors2_for_1N(estmilist):
    err = 0
    for i in range(len(estmilist)):
        err += 1/len(estmilist)*pow(estmilist[i]-1,2)
    return err





if __name__ == "__main__":
    z = 11
    x0 = 0.142421
    # errmilist = []
    # for n in nlist:
    #     tmp = errors2_for_1N(ests2_for_T(x0list2,n))
    #     errmilist.append(tmp)
    # errmilist = np.stack(errmilist)
    # print(errmilist)
    # plt.figure(1)
    # plt.plot(nlist,errmilist)
    # plt.show()

    T = eliminateCauchy(10000)
    val1 = est_mi(T)
    print(val1)
    val2 = s2n(T,1)
    print(val2)
    val3 = S2N(T,1)
    print(val3)
    # list1 = np.stack(list1)
    # list2 = np.stack(list2)
    # list3 = np.stack(list3)
    # plt.figure(1)
    # plt.plot(list1)
    # plt.show()

    # for n in nlist:
    #     for x0 in x0list:
    #         T = eliminate4(n,x0)
    #         val1 = est_mi(T)
    #         list1.append(val1)
    #
