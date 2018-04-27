import tensorflow as tf
import numpy as np

#train_X = np.random.rand(100).astype(np.float32)
#train_Y = 2 * train_X + 100
train_X = np.asarray([1,2,3,4]).astype(np.float32)
train_Y = np.asarray([3,5,7,9])


W = tf.Variable(tf.random_uniform([1]))
b = tf.Variable(tf.random_uniform([1]))

Y = W * train_X + b
cost = tf.reduce_sum(tf.square(Y - train_Y) / (2 * train_X.shape[0]))
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(100000):
        sess.run(train)

    print('W={0} b={1} cost={2:.9f}'.format(sess.run(W), sess.run(b), sess.run(cost)))


