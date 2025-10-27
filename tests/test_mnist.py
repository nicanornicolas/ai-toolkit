import pytest
import numpy as np
import tensorflow as tf

# Import the functions to be tested
from part2_practical.task2_mnist_cnn.mnist_pipeline import (
    load_and_preprocess_data,
    build_cnn_model,
    make_prediction_with_model
)

def test_load_and_preprocess_data():
    """Tests if the data loading and preprocessing works as expected."""
    (x_train, _), (x_test, _) = load_and_preprocess_data()
    
    # Check shape (should have 4 dimensions: samples, height, width, channels)
    assert x_train.shape[1:] == (28, 28, 1)
    assert x_test.shape[1:] == (28, 28, 1)
    
    # Check data type
    assert x_train.dtype == np.float32
    
    # Check normalization (pixel values should be between 0 and 1)
    assert x_train.min() >= 0.0
    assert x_train.max() <= 1.0

def test_build_cnn_model():
    """Tests the model architecture."""
    model = build_cnn_model()
    
    # Check if it's a Keras model
    assert isinstance(model, tf.keras.Model)
    
    # Check if the output layer has 10 neurons (for 10 digits)
    assert model.layers[-1].output_shape == 10
    
    # Check if the model is compiled
    assert model.optimizer is not None
    assert model.loss is not None

def test_prediction_logic():
    """
    Tests the prediction function on a dummy model and dummy data.
    This ensures the input/output flow is correct.
    """
    # Build a model for testing purposes
    model = build_cnn_model()
    
    # Create a dummy image (1 sample, 28x28 pixels, 1 channel)
    dummy_image = np.zeros((1, 28, 28, 1), dtype=np.float32)
    
    # Make a prediction
    predicted_digit = make_prediction_with_model(model, dummy_image)
    
    # The prediction should be an integer between 0 and 9
    assert isinstance(predicted_digit, np.int64) or isinstance(predicted_digit, int)
    assert 0 <= predicted_digit <= 9