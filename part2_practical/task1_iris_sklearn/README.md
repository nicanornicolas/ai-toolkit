# Task 2.1: Iris Species Classifier with Scikit-learn

## Overview
This module implements a classical machine learning pipeline to classify the species of Iris flowers using a **Decision Tree Classifier**. The goal is to demonstrate proficiency in data preprocessing, model training, and evaluation with the Scikit-learn library.

## Files in this Directory
- `iris_classifier.ipynb`: A Jupyter Notebook containing the complete end-to-end workflow, from data loading to model evaluation.

## How to Run
1. Ensure you have the project's dependencies installed from the main `requirements.txt` file.
2. Open the `iris_classifier.ipynb` notebook in a Jupyter environment (like Jupyter Lab or VS Code).
3. Execute the cells sequentially by selecting "Run All".

## Key Results
The model was evaluated on a test set (20% of the total data) and achieved excellent performance:

- **Accuracy:** 100%
- **Precision (Weighted):** 100%
- **Recall (Weighted):** 100%

The confusion matrix below confirms that there were zero misclassifications on the unseen test data.

![Iris Confusion Matrix](./screenshots/iris_confusion_matrix.png)
*(Note: You will need to take a screenshot of the confusion matrix from your notebook and save it as `iris_confusion_matrix.png` inside a new `screenshots` folder within this directory.)*

## Dependencies
- `scikit-learn`
- `pandas`
- `matplotlib`
- `seaborn`