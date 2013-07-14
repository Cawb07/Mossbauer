from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

voltages = np.genfromtxt('Iron_voltages.csv', delimiter='"')
print voltages

grossrates = np.genfromtxt('Iron_grossrates.csv', delimiter='"')
print grossrates

# Define model function to be used to fit to the data above:
def gauss(x, *p):
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))+83

# p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
p0 = [-43., 0.07, 1.5]

#coeff, var_matrix = curve_fit(gauss, velocities, grossrates, p0=p0)

#gauss_fit = gauss(velocities, *coeff)

plt.plot(voltages, grossrates, 'ro')
#plt.plot(velocities, gauss_fit)
#plt.axis([-2, 2, 40, 90])

plt.xlabel('Voltages')
plt.ylabel('Gross Counting Rates')
plt.title('Iron Absorption Spectrum')
plt.show()
