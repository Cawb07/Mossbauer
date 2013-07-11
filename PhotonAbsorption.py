import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

densities = np.array([ 1.1, 2.9, 7.5, 18.0,
             43.0, 83.0, 150.0])

voltages = np.array([1.554-0.14, 1.402-0.14, 1.191-0.14,
                     0.825-0.14, 0.476-0.14, 0.303-0.14,
                     0.171-0.14])

def exp(x, *p):
    I, b, c = p
    return I * np.exp(-b * x) + c

p0 = [1.4, .5, 0]

coeff, var_matrix = curve_fit(exp, densities, voltages, p0=p0)

exp_fit = exp(densities, *coeff)

plt.plot(densities, voltages, "ro")
plt.plot(densities, exp_fit)
plt.plot(densities, voltages)


plt.xlabel("Density x E16 in atoms/cubic meter")
plt.ylabel("Detector Output in Volts")
plt.show()