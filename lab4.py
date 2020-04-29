from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from labgotowe import random


def function41(x):
    if 0 <= x <= 1:
        tmp = 2*x
    else:
        tmp = 0
    return tmp

def eliminate41(n):
    tmplist = []
    d = 2
    num_of_elements = 0
    i = 0
    u2 = d*random(0.1231231213, 11, 3*n)
    u1 = random(0.14421322321,15,3*n)
    while(num_of_elements<n):
        if u2[i] <= function41(u1[i]):
            tmplist.append(u1[i])
            num_of_elements += 1
        i+=1
    return tmplist

def emp_dist_42(tab,x):
    value = 0
    for i in range(len(tab)):
        if (tab[i]<=x):
            value += 1/len(tab)
    return value



if __name__ == "__main__":
    print("cos")
    tmp = np.stack(eliminate41(100))
    print(emp_dist_42(tmp,0.9))