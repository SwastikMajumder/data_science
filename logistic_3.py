import random
import numpy as np
arr_x=[[0, 0], [0, 1], [1, 0], [1, 1]]
arr_y=[0, 0, 0, 0]
alpha, beta, gamma, epoch, lr = 0, 0, 0, 1000, 0.1
def sigmoid(z):
    return 1/(1+np.exp(-z))
print("Logistic Regression")
print()
for k in range(0, 3):
    if k == 0:
        arr_y = [0, 1, 1, 1]
        print("OR gate")
    elif k == 1:
        arr_y = [0, 0, 0, 1]
        print("AND gate")
    elif k == 2:
        arr_y = [0, 1, 1, 0]
        print("XOR gate")
    for i in range(0, epoch):
        par_a, par_b, par_g = 0, 0, 0
        for j in range(0, 4):
            par_a += arr_y[j] - sigmoid(alpha + beta*arr_x[j][0] + gamma*arr_x[j][1])
            par_b += arr_x[j][0] * (arr_y[j] - sigmoid(alpha + beta*arr_x[j][0] + gamma*arr_x[j][1]))
            par_g += arr_x[j][1] * (arr_y[j] - sigmoid(alpha + beta*arr_x[j][0] + gamma*arr_x[j][1]))
        par_a = -par_a
        par_b = -par_b
        par_g = -par_g
        alpha = alpha - lr*par_a
        beta = beta - lr*par_b
        gamma = gamma - lr*par_g
    print(sigmoid(alpha))
    print(sigmoid(alpha+gamma))
    print(sigmoid(alpha+beta))
    print(sigmoid(alpha+beta+gamma))
    print()
    alpha, beta, gamma = 0, 0, 0
