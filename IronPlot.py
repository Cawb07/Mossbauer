from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

voltages = np.genfromtxt('Iron_voltages.csv', delimiter='"')
print voltages

counts = np.genfromtxt('Iron_counts.csv', delimiter='"')
print counts

plt.plot(voltages, counts, 'ro')

plt.xlabel('SWS Voltage')
plt.ylabel('Gross Counts')
plt.title('Iron Absorption Spectrum')
plt.show()
