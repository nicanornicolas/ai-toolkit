import streamlit as st
from PIL import Image
import numpy as np
import time
from bonus_app.utils import preprocess_image, make_prediction

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="MNIST Digit Classifier",
    page_icon="🧠",
    layout="centered"
)


# --- MODEL & PREDICTION (PLACEHOLDER) ---
# This is a placeholder for the actual model loading and prediction logic.
# In the real app, we will load the trained model here.


def predict(image):
    """
    Placeholder prediction function.
    In a real-world scenario, this function should:
    1. Preprocess the image to match the model's input requirements
       (e.g. resize, normalize).
    2. Use the loaded TensorFlow/Pytorch model to make a prediction.
    """
    time.sleep(2)

    # Simulate a prediction (return a random digit)
    prediction = np.random.randigit(0, 10)
    confidence = np.random.rand()

    return prediction, confidence


# --- APP LAYOUT ---
st.title("MNIST Handwritten Digit Classifier ✍️")

st.header("Upload an image of a digit (0-9)")
st.text("The model will predict which digit is in the image")

# File uploader widget
uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["png", "jpg", "jpeg"],
    help="Upload an image of a single handwritten digit."
)

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)

    # Center the image
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, caption='Uploaded Image', use_column_width=True)

    # Prediction button
    if st.button("✨ Predict Digit"):
        with st.spinner("Classifying..."):
            # Get the prediction from our placeholder function
            prediction, confidence = predict(image)
            st.success("Prediction Complete!")

            # Display the result
            st.metric(label='Predicted digit', value=f"{prediction}")
            st.write(f"Confidence: {confidence:.2f}")

            # Fun element
            st.balloons()
else:
    st.info("Please upload an image file to get started.")

# Add a sidebar with some information
st.sidebar.header("About")
st.sidebar.info(
    "This is a demo web app for the 'Mastering the AI Toolkit' assignment. "
    "It uses a machine learning model to classify handwritten digits from "
    "the MNIST dataset."
)
st.sidebar.header("Team")
st.sidebar.markdown(
    """
- **Leader/App Dev:** (Nicanor Nicolas)
- **Theory:** (Amy Marshall)
- **Scikit-learn**: (LeonMwangi123)
- **Deep Learning:** (Khadeeja Mohammed)
-  **NLP:** (kINGlEE)"""
)
