import tensorflow as tf
import tensorflow.contrib.eager as tfe
import numpy as np

print(tf.__version__)
print("Setting Eager mode...")
tfe.enable_eager_execution()
print(tf.executing_eagerly())

tf_matrix0 = tf.constant([[1, 2], [3, 4]])
b = tf.add(tf_matrix0, 1)

np_matrix0 = np.array([[1, 2], [3, 4]])

print(tf_matrix0*tf_matrix0)
print(tf.multiply(tf_matrix0, tf_matrix0))
print(tf.matmul(tf_matrix0, tf_matrix0))

print(np_matrix0*np_matrix0)
print(np.multiply(np_matrix0, np_matrix0))
print(np.matmul(np_matrix0, np_matrix0))
