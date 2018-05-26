from keras import layers, models

x = layers.Input(shape=(Nin,))
h = layers.Activation('relu')(layers.Dense(Nh)(x))


class Dense:
    def __call__(self, x):
        print(x)
