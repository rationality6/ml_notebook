import tensorflow as tf
import tensorflow.contrib.eager as tfe
import numpy as np

print("Setting Eager mode...")
tfe.enable_eager_execution()
print(tf.executing_eagerly())

a = tf.constant([[1, 2], [3, 4]])
b = tf.add(a, 1)

