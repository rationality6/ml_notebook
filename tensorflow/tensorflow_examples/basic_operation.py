# from __future__ import print_function

import tensorflow as tf
import numpy as np

a = tf.constant(2)
b = tf.constant(3)

# with tf.Session() as sess:
#     print("a=2,b=3")
#     print("Addition with constants: {}".format(sess.run(a+b)))
#     print("Addition with constants: {}".format(sess.run(a)))

sess = tf.Session()

print(sess.run(a+b))
print(sess.run(a))
print(sess.run(b))
print(sess.run(a*b))

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a, b)
mul = tf.multiply(a, b)

print(sess.run(add, feed_dict={a: 2, b: 3}))
print("multi {}".format(sess.run(mul, feed_dict={a: 2, b: 3})))

matrix0 = tf.constant([[3., 3.]])
matrix1 = tf.constant([[2.], [2.]])

c = tf.placeholder(tf.float32)
d = tf.placeholder(tf.float32)

product = tf.matmul(matrix1, matrix0)
product1 = tf.matmul(matrix0, matrix1)
product2 = tf.matmul(c, d)

result = sess.run(product)
result1 = sess.run(product1)
result2 = sess.run(product2, feed_dict={c: [[3., 3.]], d: [[4], [3]]})
print(result)
print(result1)
print(result2)
