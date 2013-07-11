from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline
import numpy as np
import matplotlib.pyplot as plt

voltages = np.genfromtxt('Steel_voltages.csv', delimiter='"')
print voltages

counts = np.genfromtxt('Steel_counts.csv', delimiter='"')
print counts

# Define model function to be used to fit to the data above:
def gauss(x, *p):
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))+21000

# p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
p0 = [-9000., 0.1, 20.]

coeff, var_matrix = curve_fit(gauss, voltages, counts, p0=p0)

gauss_fit = gauss(voltages, *coeff)
print np.max(gauss_fit)
print np.std(voltages)

#spline = UnivariateSpline(voltages, -gauss_fit+np.max(gauss_fit)/2, s=0)
spline = UnivariateSpline(voltages, -counts+np.max(counts)/2, s=0)
r1, r2 = spline.roots()

plt.plot(voltages, counts, 'ro')
plt.plot(voltages, gauss_fit)
plt.axvspan(r1, r2, facecolor='g', alpha=0.5)

plt.xlabel('SWS Voltage')
plt.ylabel('Gross Counts')
plt.title('Steel Absorption Spectrum')
plt.show()
