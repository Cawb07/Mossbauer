from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

voltages = np.genfromtxt('Iron_voltages.csv', delimiter='"')
print voltages

counts = np.genfromtxt('Iron_counts.csv', delimiter='"')
print counts

# Define model function to be used to fit to the data above:
def gauss(x, *p):
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))+21000

# p0 is the initial guess for the fitting coefficients (A, mu, and sigma above)
p0 = [-9000., 0.1, 20.]

coeff, var_matrix = curve_fit(gauss, voltages, counts, p0=p0)

gauss_fit = gauss(voltages, *coeff)

plt.plot(voltages, counts, 'ro')
plt.plot(voltages, gauss_fit)

plt.xlabel('SWS Voltage')
plt.ylabel('Gross Counts')
plt.title('Iron Absorption Spectrum')
plt.show()
