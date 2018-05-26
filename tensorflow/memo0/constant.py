import tensorflow as tf
# import tensorflow.contrib.eager as tfe
# import numpy as np

# print("Setting Eager mode...")
# tfe.enable_eager_execution()
# print(tf.executing_eagerly())



node0 = tf.constant(3, tf.float32)
node1 = tf.constant(4, tf.float32)
node2 = tf.add(node0, node1)
print(node0)
print(node1)
print(node2)

hello = tf.constant("foo!")

sess = tf.Session()

print(sess.run(node0))
print(sess.run(node1))
print(sess.run(node2))
print(sess.run(hello))
