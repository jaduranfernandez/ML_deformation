import json
from dotmap import DotMap
import os
import time
from utils import get_args



def get_config_from_json(json_file):
    """
    Get the config from a json file
    :param json_file:
    :return: config(namespace) or config(dictionary)
    """
    # parse the configurations from the config json file provided
    with open(json_file, 'r') as config_file:
        config_dict = json.load(config_file)
    # convert the dictionary to a namespace using bunch lib
    config = DotMap(config_dict)
    return config, config_dict


def process_config(json_file):
    config, _ = get_config_from_json(json_file)
    config.callbacks.log_dir = os.path.join("experiments", time.strftime("%Y-%m-%d/",time.localtime()), config.exp.name, "logs/")
    config.callbacks.checkpoint_dir = os.path.join("experiments", time.strftime("%Y-%m-%d/",time.localtime()), config.exp.name, "checkpoints/")
    return config





class ConfigParser:

    def __init__(self):
        """        
        Class to parse configuration json file. Handles hyperparameters for training, initializations of modules, checkpoint saving
        and logging module.
        :param json_file: JSON File that stores the configuration for the model.
        """        
        try:
            args = get_args()   # capture the config path from the run arguments
            self.json_file = args.config
            self.process_config()
        except:
            raise NameError("Missing or invalid arguments")
            

    def process_config(self):

        with open(self.json_file, 'r') as config_file:
            config_dict = json.load(config_file)
        # convert the dictionary to a namespace using bunch lib
        self.config = DotMap(config_dict)        
        self.config.callbacks.log_dir = os.path.join("\\experiments", time.strftime("%Y-%m-%d\\",time.localtime()), self.config.exp.name, "logs\\")
        self.config.callbacks.checkpoint_dir = os.path.join("experiments", time.strftime("%Y-%m-%d\\",time.localtime()), self.config.exp.name, "checkpoints\\")


    
    def init_obj(self, obj_name, module, *args, **kwargs):
        """
        Finds a function handle with the name given as 'type' in config, and returns the
        instance initialized with corresponding arguments given.

        `object = config.init_obj('name', module, a, b=1)`
        is equivalent to
        `object = module.name(a, b=1)`
        """
        method = getattr(module, obj_name)
        return method(*args)
    
    def __getitem__(self, name):
        """Access items like ordinary dict."""
        return self.config.name

    def __getattr__(self, name):
        """Access items using variable"""
        if name in self.config:
            return getattr(self.config, name)
        else:
            raise AttributeError(f"'ConfigParser' object or '{self.json_file}' file has no attribute '{name}'")

