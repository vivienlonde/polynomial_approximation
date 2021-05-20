from chebyshev_interpolation import nb_plot_points, X_plot, Y_f_plot
from chebyshev_interpolation import Y_P_plot as Y_chebyshev_plot
from polynomial_fit import Y_P_plot as Y_polyfit_plot
import matplotlib.pyplot as plt


plt.plot(X_plot, Y_f_plot, label='f')
plt.plot(X_plot, Y_chebyshev_plot, label = 'Chebyshev')
plt.plot(X_plot, Y_polyfit_plot, label = 'Polyfit')
plt.legend()
plt.show()