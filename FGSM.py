from tensorflow import keras
from tensorflow.keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print("x_train.shape: {}".format(x_train.shape))
print("x_test.shape: {}".format(x_test.shape))
