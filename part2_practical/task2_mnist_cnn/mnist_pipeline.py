import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

def load_and_preprocess_data():
    """Loads the MNIST dataset and preprocesses it for the CNN."""
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    
    # Normalize pixel values to be between 0 and 1
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0
    
    # Reshape images to have a single channel dimension
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)
    
    return (x_train, y_train), (x_test, y_test)

def build_cnn_model(input_shape=(28, 28, 1), num_classes=10):
    """Builds, compiles, and returns a sequential CNN model."""
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

# This is a helper for testing the prediction logic
def make_prediction_with_model(model, image_array):
    """Makes a prediction on a single preprocessed image array."""
    prediction_probs = model.predict(image_array)
    predicted_digit = np.argmax(prediction_probs[0])
    return predicted_digit