from __future__ import print_function

import tensorflow as tf

hello = tf.constant("Hello, TensorFlow")

sess = tf.Session()

print(sess.run(hello))