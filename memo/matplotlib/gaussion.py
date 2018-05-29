import numpy as np
import matplotlib.pyplot as plt

mean = 0
std = 1
variance = np.square(std)
x = np.arange(-5, 5, 0.01)

f = np.exp(-np.square(x-mean)/2*variance)/(np.sqrt(2*np.pi*variance))

plt.plot(x, f)
plt.ylabel('gaussian distribution')
plt.show()

