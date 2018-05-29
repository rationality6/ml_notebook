import matplotlib.pyplot as plt
x = [*range(-3, 2)]
y = [*map(lambda g:(1 / (3**g)) + g, x)]
plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
x = [*range(-2, 3)]
y = [*map(lambda g:((1 / 8) * g**3) - (g**2), x)]
plt.plot(x, y)
plt.show()

import math
import matplotlib.pyplot as plt
x = [*range(-2, 3)]
y = [*map(lambda g:math.cos * g, x)]
plt.plot(x, y)
plt.show()


import math
import matplotlib.pyplot as plt
x = [*range(740)]
y = [*map(lambda g:math.sin(math.radians(g)), x)]
y1 = [*map(lambda g:math.cos(math.radians(g)), x)]
plt.plot(x, y)
plt.plot(x, y1)
plt.show()
