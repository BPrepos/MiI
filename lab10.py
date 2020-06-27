import numpy as np
import matplotlib.pyplot as plt
from labgotowe import random

D = 10
N = 100
L = 20
var = 1
tab_n = np.linspace(10, 110, 50).astype(int)
b = [1, 0.8, 0.6, 0.4, 0.2]
S = 5

if __name__ == "__main__":
    #generate Zn
    Zn = np.zeros(N)
    for i in range(len(Zn)):
        Zn[i] = np.random.normal(0, var)
    U_vector = np.zeros(N+S)
    for i in range(len(U_vector)):
        U_vector[i] = np.random.normal(0,1)
    Un = np.zeros((N,S),dtype=float)
    for s in range(S):
        for i in range(N):
            Un[i][s] = U_vector[i-s]
    Yn = np.dot(Un,b)+Zn
    print(Yn)
    a_est = np.dot(np.dot(np.linalg.inv(np.dot(Un.transpose(), Un)), Un.transpose()), Yn)
    print(a_est)
    error_tab = []
    Zn = np.zeros((L, N))
    for l in range(L):
        for i in range(N):
            Zn[l][i] = np.random.normal(0, var)

    # Zn = np.zeros((L,N),dtype=float)
    # tab_epsilon = np.zeros((L,N+1),dtype=float)
    # for l in range(L):
    #     for i in range(N):
    #         tab_epsilon[l][i] = np.random.normal(0, var)
    # for l in range(L):
    #     for i in range(N):
    #         Zn[l][i] = tab_epsilon[l, i + 1] - 0.5 * tab_epsilon[l, i]

    for n in tab_n:
        u_tmp = Un[:n,:]
        error = 0
        for l in range(L):
            z_tmp = Zn[l][:n]
            y_tmp = np.add(u_tmp.dot(b), z_tmp)
            a_estimated_tmp = np.dot(np.dot(np.linalg.inv(np.dot(u_tmp.transpose(),u_tmp)),u_tmp.transpose()),y_tmp)
            error += 1/L * pow((np.linalg.norm(a_estimated_tmp-b)),2)
        error_tab.append(error)
    print(error_tab)
    R = np.zeros((N,N),dtype=float)
    for i in range(N):
        for j in range(N):
            if i==j:
                R[i][j] = (1+pow(0.5 ,2))*var
            elif np.absolute(i-j)==1:
                R[i][j] = 0.5*var
    uo_est = np.dot(np.dot(np.dot(np.linalg.inv(np.dot(np.dot(Un.transpose(), np.linalg.inv(R)),Un)), Un.transpose()), np.linalg.inv(R)), Yn)
    print((uo_est))
    error_tab_2 = []
    for n in tab_n:
        u_tmp = Un[:n,:]
        error = 0
        for l in range(L):
            z_tmp = Zn[l][:n]
            y_tmp = np.add(u_tmp.dot(b), z_tmp)
            a_estimated_tmp = np.dot(np.dot(np.linalg.inv(np.dot(u_tmp.transpose(),u_tmp)),u_tmp.transpose()),y_tmp)
            error += 1/L * pow((np.linalg.norm(uo_est-b)),2)
        error_tab_2.append(error)
    print(error_tab_2)
    plt.figure(1)
    plt.plot(tab_n,error_tab)
    plt.show()