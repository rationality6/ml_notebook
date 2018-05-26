import tensorflow as tf
import tensorflow.contrib.eager as tfe
import numpy as np

print("Setting Eager mode...")
tfe.enable_eager_execution()

print(tf.executing_eagerly())


matrix0 = np.array([[2, 3]])
matrix1 = np.array([[2], [3]])
print(matrix0*matrix1)
print(np.matmul(matrix0, matrix1))
print(matrix1*matrix0)
print(np.matmul(matrix1, matrix0))
