import pytest
import numpy as np
from PIL import Image
from bonus_app.utils import preprocess_image, make_prediction

def test_preprocess_image():
    """
    Tests that the image preprocessing function returns the correct shape and type.
    """
    # Create a dummy black image (3 channels, 100x100 pixels)
    dummy_image = Image.fromarray(np.zeros((100, 100, 3), dtype=np.uint8))
    
    processed_image = preprocess_image(dummy_image)
    
    assert isinstance(processed_image, np.ndarray)
    # Check for the shape your model expects (e.g., TensorFlow with channels last)
    assert processed_image.shape == (1, 28, 28, 1)
    # Check that pixel values are normalized (between 0 and 1)
    assert processed_image.min() >= 0.0
    assert processed_image.max() <= 1.0

def test_make_prediction_placeholder():
    """
    Tests the placeholder prediction function. When you add your real model,
    you would test that it returns a valid digit and confidence.
    """
    # Create dummy processed data
    dummy_processed_image = np.zeros((1, 28, 28, 1))
    
    digit, confidence = make_prediction(dummy_processed_image)
    
    assert isinstance(digit, int)
    assert 0 <= digit <= 9
    assert isinstance(confidence, float)
    assert 0.0 <= confidence <= 1.0