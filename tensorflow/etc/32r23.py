import numpy as np


def mean_squared_error(y, t):
    return ((y-t)**2).mean(axis=None)


def cross_entrypy_error(y, t):
    if 1 == y.ndim:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)
    delta = 1e-7
    return -np.sum(np.log(y+delta)*t)/y.shape[0]


y = [0.15, 0.30, 0.45]
t = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

S = []
for i in range(len(t)):
    S.append(mean_squared_error(np.array(y), np.array(t[i])))

print(S)
print("np.min(S)   : " + str(np.min(S)))
print("np.argmin(S): " + str(np.argmin(S)))
print("np.max(S)   : " + str(np.max(S)))
print("np.argmax(S): " + str(np.argmax(S)))
