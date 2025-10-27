# Bonus Task: MNIST Digit Classifier Web App

## Overview
This directory contains a simple web application built with **Streamlit** to serve the trained MNIST CNN model. The application provides a user-friendly interface where a user can upload an image of a handwritten digit, and the app will preprocess it and display the model's prediction in real-time.

## Files in this Directory
- `app.py`: The main Streamlit application script. It handles the user interface, image preprocessing, and model inference.
- `requirements.txt`: A dedicated list of Python packages required to run this specific application.
- `README.md`: This documentation file.

## How to Run Locally

### Prerequisites
1.  **Install Dependencies:** Ensure you have installed all dependencies from the main project's `requirements.txt` file. This app specifically requires `streamlit`, `tensorflow`, `numpy`, and `Pillow`.
2.  **Trained Model:** This application depends on the trained model file from Part 2.2. Make sure the model `mnist_cnn_model.h5` exists in the following path relative to the project root:
    ```
    part2_practical/task2_mnist_cnn/models/mnist_cnn_model.h5
    ```
    If the file is missing, you must run the `mnist_cnn.ipynb` notebook to generate and save it.

### Launching the App
1.  Navigate to the **root directory** of the `ai-toolkit` project in your terminal.
2.  Run the following command:
    ```bash
    streamlit run bonus_app/app.py
    ```
3.  Your default web browser should automatically open a new tab with the application running.

## Screenshot
Below is a screenshot of the running application:

![Streamlit App Screenshot](./screenshots/streamlit_app.png)
*(Note: You will need to take a screenshot of your running Streamlit app and save it as `streamlit_app.png` inside a new `screenshots` folder within this `bonus_app` directory.)*

## Live Demo
The application has been deployed and is accessible via the following link:

**[Launch the Live App](https://your-streamlit-app-link.streamlit.app/)**
*(Note: Replace this with the actual URL after deploying your app to a service like Streamlit Community Cloud.)*

## Dependencies
- `streamlit`
- `tensorflow`
- `numpy`
- `Pillow`