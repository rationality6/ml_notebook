import tensorflow as tf
import tensorflow.contrib.eager as tfe
import numpy as np

# print("Setting Eager mode...")
# tfe.enable_eager_execution()
# print(tf.executing_eagerly())

node0 = tf.placeholder(tf.float32)
node1 = tf.placeholder(tf.float32)

adder = tf.add(node0, node1)

sess = tf.Session()

print(sess.run(adder, feed_dict={node0: [1, 3], node1: [2, 4]}))
