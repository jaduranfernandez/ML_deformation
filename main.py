from utils import get_args, process_config, create_dirs
import utils.custom as custom_fun




"""
"functions":{
    "custom": "custom_fun",
    "add": "add_fun",
    "negative": "negative_fun"
}
"""



def init_obj(config, name, module, *args, **kwargs):
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



def main():
    
    # capture the config path from the run arguments
    # then process the json configuration file
    try:
        args = get_args()
        config = process_config(args.config)
    except:
        print("missing or invalid arguments")
        exit(0)
    

    init_obj(config, "function", custom_fun )
    print(config.exp.name)



    # create the experiments dirs
    #create_dirs([config.callbacks.log_dir, config.callbacks.checkpoint_dir])




    """ print('Create the data generator.')
    data_loader = SimpleMnistDataLoader(config)

    print('Create the model.')
    model = SimpleMnistModel(config)

    print('Create the trainer')
    trainer = SimpleMnistModelTrainer(model.model, data_loader.get_train_data(), config)

    print('Start training the model.')
    trainer.train() """

if __name__ == '__main__':
    main()