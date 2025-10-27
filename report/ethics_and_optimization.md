# Part 3: Ethics & Optimization

This document provides a detailed analysis for the third part of the assignment, covering both the ethical considerations of our models and the solution to the troubleshooting challenge.

## 1. Ethical Considerations: Bias in AI Models

For this analysis, we will focus on the **Amazon Reviews NLP Model** from Part 2.3, as text data is particularly susceptible to nuanced human biases.

### Potential Biases Identified

Our rule-based NLP model is vulnerable to several types of bias:

1.  **Demographic & Cultural Bias:**
    - **Problem:** The sentiment of a review can be heavily influenced by the writer's dialect, age, and cultural context. Our keyword lists (`positive_keywords`, `negative_keywords`) are based on standard English and would likely fail to capture the sentiment of regional slang, sarcasm, or culturally specific phrases.
    - **Impact:** The model could systematically misclassify reviews from non-standard English speakers, leading to skewed sentiment analysis for certain user groups.

2.  **Reporting Bias:**
    - **Problem:** Users are most motivated to leave a review when their experience is either extremely positive or extremely negative. This creates a dataset that under-represents moderate, neutral, or nuanced opinions.
    - **Impact:** Our model, and any model trained on this data, would be very good at detecting strong emotions but poor at understanding subtlety, classifying most nuanced reviews as "Neutral".

3.  **Linguistic Bias:**
    - **Problem:** Our simple rule-based system favors explicit keywords. It cannot understand sentiment conveyed through complex sentence structures or implicit comparisons.
    - **Impact:** The model is biased towards plainly written reviews and may fail on reviews written by users with a more advanced vocabulary or writing style.

### Mitigation Strategies

**Using spaCy’s Rule-Based Systems (Our Implemented Approach):**
The primary strength of our rule-based system is its **transparency**, which is a powerful tool for mitigating bias.

-   **Manual Augmentation:** If we identify that our system is biased against a certain dialect, we can directly audit and expand our keyword lists. For example, we could add regional slang or phrases to our positive/negative lists to make the system more inclusive and accurate for different user groups.
-   **Contextual Rules with `Matcher`:** To combat linguistic bias, we can move beyond simple keywords. Using spaCy's `Matcher`, we can create more complex rules that look for grammatical patterns. For instance, we could create a rule to detect potential sarcasm by identifying a positive adjective followed by a contrasting phrase (e.g., "This product is *amazing*... if you want it to break in a week."). This allows us to manually encode a more nuanced understanding of language.

**Using TensorFlow Fairness Indicators (For a Hypothetical DL Model):**
If we were to train a deep learning sentiment model instead, we could use a tool like **TensorFlow Fairness Indicators (TF Fairness)**.

-   **Quantifying Bias:** Assuming we had metadata about the reviewers (e.g., country, self-reported language), we could use TF Fairness to slice our evaluation data. This would allow us to calculate and compare key metrics (like False Positive Rate) across different demographic groups.
-   **Identifying Disparities:** The tool would generate visualizations that make it immediately obvious if our model is systematically underperforming for a specific group. For example, it might show a much higher error rate for reviews written in British English vs. American English.
-   **Informing Remediation:** Once a bias is quantified, we can take action. This might involve collecting more data from the underrepresented group, or using techniques like re-weighting the training data to give more importance to samples from the underperforming group.

---

## 2. Troubleshooting Challenge: Debugging a TensorFlow Script

The challenge involved debugging a provided TensorFlow script with multiple errors. Below is a summary of the buggy code, the corrected code, and an explanation of each fix.

### The Buggy Code
```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# 1. DATA
X_train = np.random.rand(100, 10)
y_train_labels = np.random.randint(0, 3, 100)
y_train = tf.keras.utils.to_categorical(y_train_labels, num_classes=3)

# 2. MODEL
model = Sequential([
    Dense(32, activation='relu', input_shape=(1,)), # BUG 1: Incorrect input shape
    Dense(16, activation='relu'),
    Dense(2, activation='softmax') # BUG 2: Incorrect number of output units
])

# 3. COMPILE
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', # BUG 3: Incorrect loss function
              metrics=['accuracy'])

# 4. TRAIN
model.fit(X_train, y_train, epochs=5, batch_size=32)


