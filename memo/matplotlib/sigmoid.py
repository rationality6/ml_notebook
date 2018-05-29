import matplotlib.pyplot as plt
import math

x = [*range(-10, 11)]
y = [*map(lambda g:1/(1+math.exp(-g)), x)]
plt.plot(x, y)
plt.show()
