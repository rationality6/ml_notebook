import matplotlib.pyplot as plt

x = [*range(-10, 11)]
print(x)
y = [*map(lambda g:max(0, g), x)]
plt.plot(x, y)
plt.show()
