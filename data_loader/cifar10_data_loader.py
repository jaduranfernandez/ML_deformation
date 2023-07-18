from base import BaseDataLoader
from keras.datasets import cifar10
from keras.utils import to_categorical


class CifarDataLoader(BaseDataLoader):
    def __init__(self, config):
        super(CifarDataLoader, self).__init__(config)
        # Cargar el conjunto de datos CIFAR-10
        (x_train, y_train), (x_test, y_test) = cifar10.load_data()

        # Preprocesar los datos
        self.X_train = x_train.astype('float32') / 255.0
        self.X_test = x_test.astype('float32') / 255.0
        self.Y_train = to_categorical(y_train)
        self.Y_test = to_categorical(y_test)

    def get_train_data(self):
        return self.X_train, self.Y_train

    def get_test_data(self):
        return self.X_test, self.Y_test
        