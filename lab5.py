import numpy as np
import matplotlib.pyplot as plt
from labgotowe import random


x0list = [0.29, 0.142321, 0.23, 0.512, 0.432, 0.42, 0.25, 0.65, 0.43, 0.23]

def normal_generator(num_of_generated):
    return np.random.normal(1, 1, num_of_generated)

def normal_dist_for_x(x, mi, sigma):
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp((-1/2)*pow((x-mi)/sigma, 2))

def rectangular_kernel(x):
    if -1/2 <= x <= 1/2:
        return 1
    else:
        return 0

def function_ix(x):
    if np.abs(x)<=1:
        return 1
    else:
        return 0

def boscar_kernel(x):
    return (1/2)*function_ix(x)

def epanechnikov_kernel(x):
    return (3/4)*(1-pow(x,2))*function_ix(x)

def kernel_estimator_for_single(kernel_type, tab, hn, x):
    tmp = 0
    for j in range(len(tab)):
        if kernel_type == "rectangular":
            tmp += 1/(len(tab)*hn)*rectangular_kernel((tab[j]-x)/hn)
        elif kernel_type == "boscar":
            tmp += 1 / (len(tab) * hn) * boscar_kernel((tab[j] - x) / hn)
        elif kernel_type == "epan":
            tmp += 1 / (len(tab) * hn) * epanechnikov_kernel((tab[j] - x) / hn)
    return tmp


def kernel_estimator(kernel_type, tab, hn, N):
    x = np.linspace(-3, 4, N)
    estimated_tab = []
    for i in range(len(x)):
        tmp = 0
        for j in range(len(tab)):
            if kernel_type == "rectangular":
                tmp += 1/(len(tab)*hn)*rectangular_kernel((tab[j]-x[i])/hn)
            elif kernel_type == "boscar":
                tmp += 1 / (len(tab) * hn) * boscar_kernel((tab[j] - x[i]) / hn)
            elif kernel_type == "epan":
                tmp += 1 / (len(tab) * hn) * epanechnikov_kernel((tab[j] - x[i]) / hn)
        estimated_tab.append(tmp)
    return x, estimated_tab


def task4(M, L, N):
    x = np.linspace(-5,5, M)
    h_tab = np.linspace(0.1, 0.2, 10)
    final_tab = []
    for h in range(len(h_tab)):
        err = 0
        for l in range(L):
            generated_tab = np.random.normal(0, 1, N)
            for m in range(M):
                err += (1/(L*M))*pow((1/(N*h_tab[h])*(kernel_estimator_for_single("rectangular", generated_tab, h_tab[h], x[m])))-normal_dist_for_x(x[m],0,1) ,2)
        final_tab.append(err)
    return h_tab, final_tab










if __name__ == "__main__":
    N = 200
    h = 0.5
    M = 100
    L = 10
    normal_tab = normal_generator(N)
    random_tab = random(0.13213421, 13, N)
    print(normal_generator(10))
    fig1, ax1 = plt.subplots(3)
    x1, y1 = kernel_estimator("rectangular", normal_tab, 0.4, N)
    ax1[0].plot(x1, y1)
    x2, y2 = kernel_estimator("rectangular", normal_tab, 1, N)
    ax1[1].plot(x2, y2)
    x3, y3 = kernel_estimator("rectangular", normal_tab, 4, N)
    ax1[2].plot(x3, y3)
    fig2, ax2 = plt.subplots(3)
    x4, y4 = kernel_estimator("rectangular", normal_tab, h, N)
    ax2[0].plot(x4, y4)
    x5, y5 = kernel_estimator("boscar", normal_tab, h, N)
    ax2[1].plot(x5, y5)
    x6, y6 = kernel_estimator("epan", normal_tab, h, N)
    ax2[2].plot(x6, y6)
    fig3, ax3 = plt.subplots(3)
    x7, y7 = kernel_estimator("rectangular", random_tab, h, N)
    ax3[0].plot(x7, y7)
    x8, y8 = kernel_estimator("boscar", random_tab, h, N)
    ax3[1].plot(x8, y8)
    x9, y9 = kernel_estimator("epan", random_tab, h, N)
    ax3[2].plot(x9, y9)
    plt.figure(4)
    x10, y10 = task4(M,L,N)
    plt.plot(x10, y10)

    plt.show()


