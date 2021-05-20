from scipy.fft import dct
from numpy.polynomial.chebyshev import chebpts1, Chebyshev, cheb2poly
from numpy.polynomial.polynomial import polyval

import math
import matplotlib.pyplot as plt
import numpy as np

#### Compute Chebyshev interpolation points of the first kind.

degree = 20
X = reversed(chebpts1(degree+1)) # on inverse l'ordre pour avoir theta croissant et non x croissant.
# print('X:', X)


#### Evaluate f at Chebyshev interpolation points.

a = -5
b = 5

def affine_transformation(x, a=a, b=b): # maps [-1,1] to [a,b]
    return (b-a)/2*x +(a+b)/2
# print(affine_transformation(a, b, -1)) # should be a
# print(affine_transformation(a, b, 1)) # should be b

def inverse_affine_transformation(y, a=a, b=b): # maps [a,b] to [-1,1]
    return 2/(b-a)*y +(a+b)/(a-b)
# print(inverse_affine_transformation(a, b, a)) # should be -1
# print(inverse_affine_transformation(a, b, b)) # should be 1

f = lambda x : max(x,0)

Y = [f( affine_transformation(x) ) for x in X]
# print('Y:', Y) 


#### Apply discrete cosine transform.

def normalized_dct(Y):
    Z = dct(Y)
    # print(Z)
    Z =  Z / len(Z)
    # print(Z)
    Z[0] = Z[0]/2
    # print(Z)
    return Z

C = normalized_dct(Y)
# print('C:', C)

#### Compute the coefficients of the Chebyshev expansion in the canonical basis.

P = cheb2poly(C)
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



######## Alternative1: use numpy.polynomial.chebyshev.Chebyshev.fit to fit data.
######## Alternative2: use numpy.polynomial.chebyshev.Chebyshev.interpolate to fit function.
######## Alternative3: use numpy.polynomial.polynomial.polyfit to fit data.