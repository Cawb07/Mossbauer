import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

time = genfromtxt('Linear_time.csv', delimiter=',')
CH1 = genfromtxt('Linear_CH1.csv', delimiter=',')
CH2 = genfromtxt('Linear_CH2.csv', delimiter=',')

print time
print CH1
print CH2

plt.plot(time, CH1)
plt.xlabel('Time in S')
plt.ylabel('Horizontal Magnetic Field Sweep in Volts')
plt.title('Field Sweep')

plt.show()