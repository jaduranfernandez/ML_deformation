
class BaseModel(object):
    def __init__(self, config):
        super(BaseModel, self).__init__()
        self.config = config
        self.model = None

    # save function that saves the checkpoint in the path defined in the config file
    def save(self, checkpoint_path):
        if self.model is None:
            raise Exception("You have to build the model first.")

        print("Saving model...")
        self.model.save_weights(checkpoint_path)
        print("Model saved")

    # load latest checkpoint from the experiment path defined in the config file
    def load(self, checkpoint_path):
        if self.model is None:
            raise Exception("You have to build the model first.")

        print("Loading model checkpoint {} ...\n".format(checkpoint_path))
        self.model.load_weights(checkpoint_path)
        print("Model loaded")

    def build_model(self):
        raise NotImplementedError
    
    def __getattr__(self, name):
        """Access items using variable"""
        if name in self.model:
            return getattr(self.model, name)
        else:
            raise AttributeError(f"'Model' object has no attribute '{name}'")