import random
import numpy as np
from matplotlib import pyplot as plt

arr_x=[]
arr_y=[]
size = 10
alpha = 0
beta = 0
epoch = 1000
lr = 0.1

def sigmoid(z):
    return 1/(1+np.exp(-z))

def sigmoid_2(x):
    return sigmoid(alpha+beta*x)

for i in range(0, size):
    arr_x.append(random.randrange(-4, 4)*random.random())
    arr_y.append(random.randrange(0, 2))

plt.scatter(arr_x, arr_y, color='r')

for i in range(0, epoch):
    par_a, par_b, = 0, 0
    for j in range(0, size):
        par_a += arr_y[j]-sigmoid(alpha+beta*arr_x[j])
        par_b += arr_x[j]*(arr_y[j]-sigmoid(alpha+beta*arr_x[j]))
    par_a = -par_a
    par_b = -par_b
    alpha = alpha - lr*par_a
    beta = beta - lr*par_b

plot_x = np.linspace(-4, 4, 100)

plt.plot(plot_x, sigmoid_2(plot_x), color='b')
plt.show()
