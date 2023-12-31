# ML_deformation: Complex Deformation Solver using Machine Learning

## Description
This project aims to apply machine learning techniques to solve complex deformations. It will be implemented in Python, using the Keras library to train the machine learning models. The following processes will be followed:

1. Read deformation data produced by MAYA, including mesh-specific data, rotations, and the number of articulations.
2. Create and train models based on user-provided configurations, which will be provided through a JSON file. Configurations include the number of neurons, loss functions, accuracy metrics, and the number of layers.
3. Once training is complete, create files to store the performance of the trained models.
4. Save each trained model locally on the user's computer.

## Requirements
To run this project, you need to have the following dependencies installed:

- Python (version 3.11.0 or higher)
- Keras (version X.X.X)
- MAYA (version X.X.X)
- dotmap

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jaduranfernandez/ML_deformation
   ```
2. Change to the project directory:
   ```bash
   cd ML_deformation
   ```
3. Install the required dependencies:
   ```bash
   pip install keras
   ```
4. Make sure you have MAYA installed and properly configured.

## Usage
1. Prepare your deformation data in a format compatible with MAYA.
2. Prepare a JSON configuration file with the necessary model training configurations. Example structure:
   ```json
   {
      "exp": {
         "name": "basic_model"
      },
      "data_loader": {
         "name": "CifarDataLoader"
      },
      "model":{
         "name": "BasicModel",
         "learning_rate": 0.01,
         "optimizer": "adam",
         "loss": "mse",
         "metrics": "accuracy"
      },
      "trainer":{
         "name": "SimpleCifarModelTrainer",
         "num_epochs": 100,
         "batch_size": 32,
         "validation_split": 0.25,
         "verbose_training": true
      },
      "callbacks":{
         "checkpoint_monitor": "val_loss",
         "checkpoint_mode": "min",
         "checkpoint_save_best_only": true,
         "checkpoint_save_weights_only": true,
         "checkpoint_verbose": true,
         "tensorboard_write_graph": true
      }
   }
   ```
3. Run the main script, providing the path to the JSON configuration file:
   ```bash
   python main.py --config config.json
   ```
4. Once the training is complete, the program will generate performance files for the trained models.
5. Each trained model will be saved locally on your computer for future use.

## Contributing
Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request in the main repository.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contact
For any questions or inquiries, please contact using this [email](mailto:jaduranfernandez@outlook.es).

Feel free to explore, use, and contribute to this project! Thank you for your interest.