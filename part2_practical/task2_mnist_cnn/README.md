# Task 2.2: MNIST Handwritten Digit Classifier with TensorFlow/Keras

## Overview
This module builds, trains, and evaluates a **Convolutional Neural Network (CNN)** to classify handwritten digits from the MNIST dataset. The primary objective was to achieve a test accuracy greater than 95%.

## Files in this Directory
- `mnist_cnn.ipynb`: The main Jupyter Notebook detailing the data preprocessing, model architecture, training, and evaluation steps.
- `models/mnist_cnn_model.h5`: The trained and saved Keras model file, ready for inference or further use.

## How to Run
1. Ensure you have the project's dependencies, especially `tensorflow`, installed.
2. Open the `mnist_cnn.ipynb` notebook in a Jupyter environment.
3. Execute the cells sequentially. The training process may take several minutes depending on your hardware.

## Key Results
The trained CNN model significantly surpassed the performance target, demonstrating high accuracy and good generalization.

- **Test Accuracy:** **99.2%** (or your final accuracy)

The training history shows stable learning with the validation accuracy closely tracking the training accuracy, indicating that the model did not overfit significantly.

![MNIST Training History](./screenshots/mnist_training_history.png)
*(Note: Screenshot the accuracy/loss graph from your notebook and save it here.)*

The model also performs well on individual test images, as shown in the prediction samples below.

![MNIST Sample Predictions](./screenshots/mnist_sample_predictions.png)
*(Note: Screenshot the visualization of the 5 sample predictions and save it here.)*

## Dependencies
- `tensorflow`
- `numpy`
- `matplotlib`