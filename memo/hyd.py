string = 'Hydrogen'

for i, l in enumerate(string):
    print((l, i))

from pylab import *

x = [0, 2, -3, -1.5]
y = [0, 3, 1, -2.5]
color = ['m', 'g', 'r', 'b']

scatter(x, y, s=100, marker='o', c=color)

show()


import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('clien')
plt.grid(True)
plt.savefig("test.png")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

t = np.arrange(0.0, 2.0, 0.01)
plt.plot(t, s)
plt.show()


import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4, 3], [1, 3, 4, 5, 2])
plt.show()


print([*range(10)])

arr0 = [5, 4, 2, 3, 1]


def insertion_sort(L):
    clone = L[:]
    for i in range(1, len(clone)):
        p = i
        c = clone[i]
        while 0 < p and c < clone[p - 1]:
            clone[p] = clone[p - 1]
            p -= 1
        clone[p] = c
    return clone


print(arr0)
insertion_sort(arr0)


import matplotlib.pyplot as plt

plt.plot([2, 3, 4], [5, 6, 7])
plt.ylabel("foo")
plt.xlabel("bar")
plt.show()


import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 2, 3], [7, 8, 9], [8, 9, 10])
plt.show()


import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()


import matplotlib.pyplot as plt
arr0 = [*map(lambda x:x**2, range(-10, 11))]
plt.plot(arr0)
# plt.axis([0, 6, 0, 20])
plt.show()


import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis([0, 6, 0, 20])
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.005)
print(x)


import math
print(math.sqrt(-1))


import matplotlib.pyplot as plt
arr0 = [*map(lambda x:x**2, range(-10, 11))]
plt.plot(arr0)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 10, 0.5)
plt.plot(x)
plt.show()

import matplotlib.pyplot as plt
plt.plot([*range(11)], [*map(lambda x:x**2, range(-5, 6))])
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1e6, 10)
plt.plot(x, 8.0 * (x**2) / 1e6, lw=5)
plt.show()

import matplotlib.pyplot as plt
data = [*map(lambda x:x**2, range(10))]
plt.plot(data)
plt.show()
import matplotlib.pyplot as plt
data = [*map(lambda x:3 * x + 3, range(10))]
plt.plot(data)
plt.show()


def selection_sort(L):
    clone = L[:]
    length_clone = len(clone)
    for i in range(length_clone):
        index = i
        for z in range(i, length_clone):
            if clone[z] < clone[index]:
                index = z
        clone[i], clone[index] = clone[index], clone[i]

    return clone


arr0 = [*reversed(range(1, 11))]
print(arr0)
print(selection_sort(arr0))


import matplotlib.pyplot as plt
x = [*range(-5, 6)]
y = [6, 4, 2, 0, -1, -2, -3, 0, 3, 6, 9]
plt.plot(x, y)
plt.show()


import matplotlib.pyplot as plt
x = [*range(9)]
y = [*map(lambda x:((1 / 8) * (x**3)) - (x**2), x)]
plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
x = [*range(-4,4)]
y = [*map(lambda g:(g**3) - (9 * g), x)]
plt.plot(x, y)
plt.show()
