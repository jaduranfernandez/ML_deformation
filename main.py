from utils import ConfigParser, create_dirs
import data_loader as loaders
import models


"""
"functions":{
    "custom": "custom_fun",
    "add": "add_fun",
    "negative": "negative_fun"
}
"""





def main():
    
    #   Obtain experiment's configuration
    config = ConfigParser()    
    print(config.exp.name)


    #   Create the experiments dirs
    create_dirs([config.callbacks.log_dir, config.callbacks.checkpoint_dir])

    
    print('Create the data generator.')
    data_loader = config.init_obj(config.data_loader.name, loaders, config)

    print('Create the model.')
    model = config.init_obj(config.model.name, models, config)
    model.model.summary()

    """


    print('Create the trainer')
    trainer = SimpleMnistModelTrainer(model.model, data_loader.get_train_data(), config)

    print('Start training the model.')
    trainer.train() """

if __name__ == '__main__':
    main()