from numpy.polynomial.polynomial import polyfit, polyval

import math
import matplotlib.pyplot as plt
import numpy as np

#### Compute data points.

degree = 20
nb_data_points = 500
X = [-1 + i*2/nb_data_points for i in range(nb_data_points+1)]
# print('X:', X)


#### Evaluate f at data points.

a = -5
b = 5

def affine_transformation(x, a=a, b=b): # maps [-1,1] to [a,b]
    return (b-a)/2*x +(a+b)/2
# print(affine_transformation(-1)) # should be a
# print(affine_transformation(1)) # should be b

def inverse_affine_transformation(y, a=a, b=b): # maps [a,b] to [-1,1]
    return 2/(b-a)*y +(a+b)/(a-b)
# print(inverse_affine_transformation(a)) # should be -1
# print(inverse_affine_transformation(b)) # should be 1

f = lambda x : max(x,0)

Y = [f( affine_transformation(x) ) for x in X]
# print('Y:', Y) 


#### Fit with a polynomial

P = polyfit(X, Y, degree)
# print('P:', P)

#### Plot f and its chebyshev interpolation approximation

nb_plot_points = 100
X_plot = [a + i*(b-a)/nb_plot_points for i in range(nb_plot_points+1)]
Y_f_plot = [f(x) for x in X_plot]
Y_P_plot = [polyval(inverse_affine_transformation(x), P) for x in X_plot]
# plt.plot(X_plot, Y_f_plot, label='f')
# plt.plot(X_plot, Y_P_plot, label = 'P')
# plt.legend()
# plt.show()



