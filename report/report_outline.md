## 1. Introduction
> **Owner: [Nicanor Nicolas - Leader]**
>
> **Task:** Write 1-2 paragraphs summarizing the project. State the objective: to demonstrate proficiency in key AI tools (Scikit-learn, TensorFlow, spaCy) through a series of practical and theoretical tasks, emphasizing teamwork and collaborative development.

---

## 2. Theoretical Understanding (Part 1)
> **Owner: [Amy Marshall]**
>
> **Task:** Integrate the final, polished answers from `part1_theory/answers.md` into this section. Ensure formatting is clean and consistent.

### 2.1 Short Answer Questions
- **Q1:** Differences between TensorFlow and PyTorch.
- **Q2:** Two use cases for Jupyter Notebooks.
- **Q3:** How spaCy enhances NLP tasks.

### 2.2 Comparative Analysis
- A comparison table for Scikit-learn vs. TensorFlow covering target applications, ease of use, and community support.

---

## 3. Practical Implementation (Part 2)

### 3.1 Task 1: Classical ML with Scikit-learn
> **Owner: [Khadeeja Mohammed]**
>
> **Task:** Write a brief summary of the task. Insert the final evaluation metrics and the confusion matrix screenshot from your notebook.

**Summary:** We built a Decision Tree classifier using Scikit-learn to predict Iris flower species. The model was trained and evaluated on the classic Iris dataset.

**Key Results:**
The model achieved perfect scores on the unseen test set, indicating its effectiveness for this dataset.

- **Accuracy:** 100%
- **Precision (Weighted):** 100%
- **Recall (Weighted):** 100%


### 3.2 Task 2: Deep Learning with TensorFlow/Keras
> **Owner: [KingLEE]**
>
> **Task:** Write a brief summary. Insert the final test accuracy, the training history plot, and the sample predictions screenshot.

**Summary:** We developed a Convolutional Neural Network (CNN) with TensorFlow to classify handwritten digits from the MNIST dataset. The goal was to exceed 95% test accuracy.

**Key Results:**
The CNN model successfully achieved a test accuracy of over 99%, far exceeding the project goal. The training history shows stable learning without significant overfitting.

### 3.3 Task 3: NLP with spaCy
> **Owner: [LeonMwangi]**
>
> **Task:** Write a brief summary. Include a code snippet and an output example from the integrated analysis pipeline.

**Summary:** We used the spaCy library to perform Named Entity Recognition (NER) and rule-based sentiment analysis on a sample of Amazon product reviews.

**Key Results:**
The pipeline successfully extracted relevant entities (brands and products) and classified the sentiment of reviews based on custom rules.

**Example Pipeline Output:**
```python
# Code Snippet
process_review("The Sony WH-1000XM5 headphones are a masterpiece of engineering.")

# Output
{'entities': {'products_brands': ['Sony WH-1000XM5']}, 'sentiment': 'Positive'}