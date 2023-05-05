import random
from matplotlib import pyplot as plt

size = 10
arr_x = []
arr_y = []
epoch = 1000 
lr = 0.1
alpha = 0
beta = 1
point_arr = []

for i in range(0, size):
    arr_x.append(random.random())
    arr_y.append(random.random())

plt.scatter(arr_x, arr_y, color='r')

for j in range(0, epoch):
    par_a, par_b = 0, 0
    for i in range(0, size):
        par_a += alpha + beta*arr_x[i] - arr_y[i]
        par_b += (alpha + beta*arr_x[i] - arr_y[i])*arr_x[i]
    alpha = alpha - lr*par_a
    beta = beta - lr*par_b

plt.plot([0, alpha], [-alpha/beta, 0], color='b')
plt.show()
