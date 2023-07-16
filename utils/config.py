import json
from dotmap import DotMap
import os
import time




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

    def __init__(self, json_file):
        """        
        Class to parse configuration json file. Handles hyperparameters for training, initializations of modules, checkpoint saving
        and logging module.
        :param json_file: JSON File that stores the configuration for the model.
        """
        self.json_file = json_file
        self.process_config()


    def process_config(self):

        with open(self.json_file, 'r') as config_file:
            config_dict = json.load(config_file)
        # convert the dictionary to a namespace using bunch lib
        self.config = DotMap(config_dict)        
        self.config.callbacks.log_dir = os.path.join("experiments", time.strftime("%Y-%m-%d/",time.localtime()), self.config.exp.name, "logs/")
        self.config.callbacks.checkpoint_dir = os.path.join("experiments", time.strftime("%Y-%m-%d/",time.localtime()), self.config.exp.name, "checkpoints/")

    
    def init_obj(self, obj_name, module, *args, **kwargs):
        """
        Finds a function handle with the name given as 'type' in config, and returns the
        instance initialized with corresponding arguments given.

        `object = config.init_obj('name', module, a, b=1)`
        is equivalent to
        `object = module.name(a, b=1)`
        """

        module_name = config[name]
        print(module_name)
        module_args = dict(config[name]['args'])
        assert all([k not in module_args for k in kwargs]), 'Overwriting kwargs given in config file is not allowed'
        module_args.update(kwargs)
        return getattr(module, module_name)(*args, **module_args)

