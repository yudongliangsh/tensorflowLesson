import tensorflow as tf
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'

var = tf.constant('hello world')
sess = tf.Session()
print(sess.run(var))

