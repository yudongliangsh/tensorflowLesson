import tensorflow as tf
import numpy as np
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'

a = tf.constant([[1,1],[1,1]])
b = tf.constant([[1,2],[3,4]])
sess = tf.Session()

print(sess.run(tf.add(a,b)))