import tensorflow as tf
# print(tf.__version__)

# hello = tf.constant("Hello, TensorFlow!")
# sess = tf.Session()
# print(sess.run(hello))

# node1 = tf.constant(3.0, tf.float32)
# node2 = tf.constant(4.0)
# node3 = tf.add(node1, node2)
#
# print("node1:", node1, "node2:", node2)
# print("node3: ", node3)
#
# sess = tf.Session()
# print("sess.run(node1, node2): ", sess.run([node1, node2]))
# print("sess.run(node3): ", sess.run(node3))

# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)
# adder_node = a + b
#
# sess = tf.Session()
#
# print(sess.run(adder_node, feed_dict={a: 3, b: 4.5}))
# print(sess.run(adder_node, feed_dict={a: [1, 3], b: [2, 4]}))

# x_train = [1, 2, 3]
# y_train = [1, 2, 3]

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

hypothesis = X * W + b
# fomular
cost = tf.reduce_mean(tf.square(hypothesis - Y))
# GradientDescent
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(20001):
    cost_val, W_val, b_val, _ = \
        sess.run([cost, W, b, train], feed_dict={
                 X: [1, 2, 3, 4, 5], Y: [2.1, 3.1, 4.1, 5.1, 6.1]})

    if step % 20 == 0:
        print(step, cost_val, W_val, b_val)
