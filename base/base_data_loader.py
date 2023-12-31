


class BaseDataLoader(object):
    """
    Base class for loading data
    """
    def __init__(self, config):
        self.config = config

    def get_train_data(self):
        raise NotImplementedError

    def get_test_data(self):
        raise NotImplementedError