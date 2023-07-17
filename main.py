from utils import ConfigParser
import utils.custom as custom_fun




"""
"functions":{
    "custom": "custom_fun",
    "add": "add_fun",
    "negative": "negative_fun"
}
"""





def main():
    
    
    config = ConfigParser()    
    print(config.exp.name)





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