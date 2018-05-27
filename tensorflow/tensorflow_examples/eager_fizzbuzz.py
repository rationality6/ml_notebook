import tensorflow as tf
import tensorflow.contrib.eager as tfe
import numpy as np

tfe.enable_eager_execution()
print(tf.executing_eagerly())


def fizzbuzz(max_num):
    counter = tf.constant(0)
    for num in range(max_num):
        num = tf.constant(num)
        if int(num % 3) == 0 and int(num % 5) == 0:
            print('FizzBuzz')
        elif int(num % 3) == 0:
            print("Fizz")
        elif int(num % 5) == 0:
            print("Buzz")
        else:
            print(num)
        counter += 1
    return counter


print(fizzbuzz(10))


def fizzbuzz(max_num):
    counter = tf.constant(0)
    for num in range(max_num):
        num = tf.constant(num)
        if int(num % 3) == 0 and int(num % 5) == 0:
            print('FizzBuzz')
        elif int(num % 3) == 0:
            print('Fizz')
        elif int(num % 5) == 0:
            print('Buzz')
        else:
            print(num)
        counter += 1
    return counter


print(fizzbuzz(10))
