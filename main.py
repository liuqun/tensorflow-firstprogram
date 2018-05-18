#!/usr/bin/env python
# -*- coding:utf-8 -*-


import tensorflow as tf

if __name__ == '__main__':
    hello = tf.constant('Hello, Tensor!')
    sess = tf.Session()
    print(sess.run(hello))
    a = tf.constant(10)
    b = tf.constant(20)
    print(sess.run(a + b))
