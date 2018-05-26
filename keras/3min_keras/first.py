import keras
import numpy as np
# keras.__version__
x = np.array([0, 1, 2, 3, 4])
y = x * 2 + 1

model = keras.models.Sequential()
model.add(keras.layers.Dense(1, input_shape=(1,)))
model.compile('SGD', 'mse')

model.fit(x[:2], y[:2], epochs=2000, verbose=1)


print('Targets:', y[2:])
print('Predictions:', model.predict(x[2:]).flatten())

