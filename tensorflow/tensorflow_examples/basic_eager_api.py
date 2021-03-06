# from __future__ import absolute_import, division, print_function

import tensorflow as tf
import tensorflow.contrib.eager as tfe
import numpy as np

print(tf.__version__)

print("Setting Eager mode...")
tfe.enable_eager_execution()

print(tf.executing_eagerly())

x = [[2.]]
m = tf.matmul(x, x)

def my_py_func(x):
  x = tf.matmul(x,x)
  print(x)
  return x

print("Hello {}".format(m))

a = tf.constant([[1, 2], [3, 4]])
print(a)

b = tf.add(a, 1)
print(b)
print(a*b)

arr0 = np.array([[1, 2], [3, 4]])
print("numpy", my_py_func(arr0, arr0))
