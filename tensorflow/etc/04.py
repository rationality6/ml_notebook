import numpy as np
import tensorflow as tf

num_points = 200
vectors_set = []

W = tf.Variable(tf.random_normal([1]), name='weight')
X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

hypothesis = X * W
# fomular
cost = tf.reduce_mean(tf.square(hypothesis - Y))
# GradientDescent
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, W_val, _ = \
        sess.run([cost, W, train], feed_dict={
                 X: [1, 2, 3, 4, 5], Y: [2.1, 3.1, 4.1, 5.1, 6.1]})

    if step % 20 == 0:
        print(step, cost_val, W_val)

import math
import matplotlib.pyplot as plt
plt.plot([*map(lambda x: math.sin(math.radians(x)), [*range(900)])])
plt.plot([*map(lambda x: math.cos(math.radians(x)), [*range(900)])])
plt.show()
