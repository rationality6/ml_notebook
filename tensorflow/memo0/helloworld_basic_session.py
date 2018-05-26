import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

i = tf.constant(10)
j = tf.constant(32)
print(sess.run(i + j))
