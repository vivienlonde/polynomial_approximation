import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit, polyval
from math import *
import os

from utilities import get_polynomial_coefficients_from_string

script_directory = os.path.dirname(os.path.abspath(__file__))

# a, b = 0.2, 4
# a, b = 0.008, 2
a, b = -1, 1
degree = 20
nb_points = 1000

X = np.linspace(a, b, nb_points)

def function(x):
    # return log(x)
    # return 1/math.sqrt(x)
    return (1+erf(10*x))/2
    # return math.sqrt(x)

# f = 'log'
# f = 'inv_sqrt'
f = 'cdf_gaussian'
# f = 'sqrt'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
def Remez_poly(x):
    coeffs = get_polynomial_coefficients_from_string(
        "5.e-1+5.0237413775077886*x-7.3134785227886942e-20*x**2-9.60434124537088e+1*x**3+4.1429681057398728e-18*x**4+1.1007849554703991e+3*x**5-7.9832526071746695e-17*x**6-7.0142823644293954e+3*x**7+7.1652092039261343e-16*x**8+2.6408333598395456e+4*x**9-3.4814178998304872e-15*x**10-6.1111122586817731e+4*x**11+9.8699137387953871e-15*x**12+8.777034687107316e+4*x**13-1.6779192852921977e-14*x**14-7.6188481917103197e+4*x**15+1.6823989921990836e-14*x**16+3.6580512883893625e+4*x**17-9.1618291291840195e-15*x**18-7.4545925899670309e+3*x**19+2.0878925719503153e-15*x**20"
        )
    res = 0
    power_of_x = 1
    for c in coeffs:
        res += c*power_of_x
        power_of_x *= x
    return res

Y = [function(x) for x in X]
# L2_poly = polyfit(X, Y, degree)
# Y_L2 = [polyval(x, L2_poly) for x in X]
Y_Remez = [Remez_poly(x) for x in X]

plt.plot(X, Y, label = 'target function : ' + f)
# plt.plot(X, Y_L2, label = 'L2 fit')
plt.plot(X, Y_Remez, label = r'L$\infty$ fit (Remez) of degree ' + str(degree))
# plt.plot(X, Y_Remez, label = r'L$\infty$ relative error fit (Remez) of degree ' + str(degree))
plt.legend()

output_directory = os.path.join(script_directory, 'plots')
# filename = os.path.join(output_directory, 'approximate_{}_degree_{}.png'.format(f, degree))
filename = os.path.join(output_directory, 'approximate_{}_degree_{}_range_8_3.png'.format(f, degree))
# filename = os.path.join(output_directory, 'approximate_{}_degree_{}_range_8_3_relative_error.png'.format(f, degree))
# filename = os.path.join(output_directory, 'approximate_{}_degree_{}_range_{}.png'.format(f, degree, b))
plt.savefig(filename)

plt.show()


# L2_error = [polyval(x, L2_poly) - max(x,0) for x in X]
# Remez_error = [Remez_poly(x) - max(x,0) for x in X]

# plt.plot(X, L2_error, label = 'L2_error')
# plt.plot(X, Remez_error, label = 'Remez_error')
# plt.legend()
# plt.show()



