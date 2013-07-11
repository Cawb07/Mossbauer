import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

time = genfromtxt('Linear_time.csv', delimiter=',')
CH1 = genfromtxt('Linear_CH1.csv', delimiter=',')
CH2 = genfromtxt('Linear_CH2.csv', delimiter=',')

print time
print CH1
print CH2

plt.plot(time, CH2)
plt.xlabel('Time in S')
plt.ylabel('Detector Output (CH2) in Volts')
plt.title('Low Field Resonances')

plt.show()