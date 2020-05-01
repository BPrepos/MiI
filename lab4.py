from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from labgotowe import random
from lab2 import finCauchy


def function41(x):
    if 0 <= x <= 1:
        tmp = 2 * x
    else:
        tmp = 0
    return tmp


def eliminate41(n):
    tmplist = []
    d = 2
    num_of_elements = 0
    i = 0
    u2 = d * random(0.1231231213, 11, 3 * n)
    u1 = random(0.14421322321, 15, 3 * n)
    while (num_of_elements < n):
        if u2[i] <= function41(u1[i]):
            tmplist.append(u1[i])
            num_of_elements += 1
        i += 1
    return tmplist

def eliminate_cauchy_upgraded(n):
    tmplist = []
    num_of_elements = 0
    i = 0
    u2 = 0.35 * random(0.1231231213, 11, 5 * n)
    u1 = 10*random(0.1221321, 11, 5*n)-5
    while (num_of_elements < n):
        if u2[i] <= finCauchy(u1[i]):
            tmplist.append(u1[i])
            num_of_elements += 1
        i += 1
    return tmplist



def emp_dist_42(tab, x):
    value = 0
    for i in range(len(tab)):
        if (tab[i] <= x):
            value += 1 / len(tab)
    return value


def calculated_dist(x):
    if x < 0:
        return 0
    elif 0 <= x <= 1:
        return pow(x, 2)
    else:
        return 1


def plot_calculated_dist_41(xmin, xmax, number_of_x):
    x = np.linspace(xmin, xmax, number_of_x)
    y = []
    for i in range(len(x)):
        y.append(calculated_dist(x[i]))
    return x, y


def plot_emp_dist(tab, xmin, xmax, number_of_x):
    x = np.linspace(xmin, xmax, number_of_x)
    generated_tab = tab
    y = []
    for i in range(len(x)):
        y.append(emp_dist_42(generated_tab, x[i]))
    return x, y


def dn(tab):
    tmp = []
    x = np.linspace(0, 1, 1000)
    for i in range(len(x)):
        tmp.append(emp_dist_42(tab, x[i]) - calculated_dist(x[i]))
        np.absolute(tmp)
    return max(tmp)


def get_44_data():
    list = []
    with (open('lab44data', 'r')) as file:
        data = file.readlines()
        for x in data:
            tmp = float(x)
            list.append(tmp)
    return list

def var_of_est(N):
    tmp = []
    x = np.linspace(-2,2,N)
    for i in range(len(x)):
        tmp.append((1/N)*calculated_dist(x[i]*(1-calculated_dist(x[i]))))
    return tmp


if __name__ == "__main__":
    fig1, ax1 = plt.subplots(2)
    fig1.suptitle("Dystrybuanta wyprowadzona i empiryczna")
    calc_dist_x, calc_dist_y = plot_calculated_dist_41(-1, 2, 100)
    ax1[0].plot(calc_dist_x, calc_dist_y)
    emp_dist_x42, emp_dist_y42 = plot_emp_dist(eliminate41(1000),-1,2,1000)
    ax1[1].plot(emp_dist_x42, emp_dist_y42)
    fig2, ax2 = plt.subplots(4)
    emp_dist_x44, emp_dist_y44 = plot_emp_dist(get_44_data(),-5, 5, 1000)
    ax2[0].plot(emp_dist_x44, emp_dist_y44)
    normal11x, normal11y = plot_emp_dist(np.random.normal(1,1,1000),-5,5,1000)
    ax2[1].plot(normal11x,normal11y)
    normal05x, normal05y = plot_emp_dist(np.random.normal(0, np.sqrt(5), 1000), -5, 5, 1000)
    ax2[2].plot(normal05x,normal05y)
    cauchy01x, cauchy01y = plot_emp_dist(eliminate_cauchy_upgraded(1000),-5,5,1000)
    ax2[3].plot(cauchy01x,cauchy01y)


    plt.show()
